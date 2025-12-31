

import xmltodict
from deriv_api import DerivAPI
import asyncio
from supabase_client import supabase
from kraken_api import KrakenAPI

from ai_council import AICouncil
from realtime_data import RealTimeData
from auto_withdraw import auto_withdraw
from compliance import log_compliance, check_kyc


class BotExecutor:
    def __init__(self, xml_path, app_id, token, kraken_key=None, kraken_secret=None, user=None):
        self.xml_path = xml_path
        self.app_id = app_id
        self.token = token
        self.api = DerivAPI(app_id, token)
        self.kraken = KrakenAPI(kraken_key, kraken_secret)
        self.council = AICouncil()
        self.data = RealTimeData()
        self.user = user or {"kyc_verified": True}
        self.config = None

    def parse_xml(self):
        with open(self.xml_path, 'r') as f:
            self.config = xmltodict.parse(f.read())
        # Extract contract info from XML
        trade_block = self.config['xml']['block']
        self.symbol = trade_block.get('field', [])[2]['#text'] if isinstance(trade_block.get('field', []), list) else None
        self.contract_type = trade_block.get('field', [])[5]['#text'] if isinstance(trade_block.get('field', []), list) else None
        # Find amount and duration from nested blocks
        submarket = trade_block.get('statement', [])[1]['block'] if isinstance(trade_block.get('statement', []), list) else None
        if submarket:
            fields = submarket.get('field', [])
            values = submarket.get('value', [])
            if isinstance(values, list):
                for v in values:
                    if v['@name'] == 'DURATION':
                        self.duration = v['block']['field']['#text'] if 'block' in v and 'field' in v['block'] else None
                    if v['@name'] == 'AMOUNT':
                        # Try to get amount from variable or number
                        if 'block' in v and v['block']['field']:
                            self.amount = 11  # fallback, real value should be parsed from variable
                        else:
                            self.amount = v['block']['field']['#text']
        # Fallbacks
        if not hasattr(self, 'amount'):
            self.amount = 1
        if not hasattr(self, 'duration'):
            self.duration = 1

    async def run(self):
        # Compliance check
        if not check_kyc(self.user):
            log_compliance("KYC_FAIL", f"User {self.user} not verified")
            return
        await self.api.connect()
        self.parse_xml()
        # Fetch real-time data from all exchanges
        kraken_price = self.data.get_kraken_ticker()
        binance_price = self.data.get_binance_ticker()
        coinbase_price = self.data.get_coinbase_ticker()
        kucoin_price = self.data.get_kucoin_ticker()
        market_data = {
            "kraken": kraken_price,
            "binance": binance_price,
            "coinbase": coinbase_price,
            "kucoin": kucoin_price
        }
        # AI council votes on trade action
        decision, votes = self.council.vote(market_data)
        # Log AI votes
        trade_id = None
        for idx, vote in enumerate(votes):
            supabase.table("ai_votes").insert({
                "trade_id": trade_id,
                "model_name": f"ai_model_{idx+1}",
                "vote": vote
            }).execute()
        if decision == "buy":
            # Prepare a simple contract proposal (example: digits differ)
            proposal = {
                "proposal": 1,
                "amount": self.amount,
                "basis": "stake",
                "contract_type": self.contract_type or "DIGITDIFF",
                "currency": "USD",
                "duration": self.duration,
                "duration_unit": "t",
                "symbol": self.symbol or "1HZ100V"
            }
            await self.api.send(proposal)
            proposal_response = await self.api.recv()
            if 'proposal' in proposal_response:
                proposal_id = proposal_response['proposal']['id']
                buy_result = await self.api.buy(proposal_id, self.amount)
                # Log trade to Supabase
                trade_insert = supabase.table("trades").insert({
                    "bot_id": None,
                    "user_id": None,
                    "symbol": self.symbol,
                    "contract_type": self.contract_type,
                    "amount": self.amount,
                    "result": str(buy_result)
                }).execute()
                trade_id = trade_insert.data[0]['id'] if trade_insert.data else None
                # Execute a Kraken trade (example: buy BTC/USD)
                kraken_result = self.kraken.add_order(pair="XXBTZUSD", type_="buy", ordertype="market", volume=str(self.amount))
                supabase.table("trades").insert({
                    "bot_id": None,
                    "user_id": None,
                    "symbol": "XXBTZUSD",
                    "contract_type": "kraken_market_buy",
                    "amount": self.amount,
                    "result": str(kraken_result)
                }).execute()
                # Auto-withdraw profits to bank if above threshold
                profit = float(buy_result.get('profit', 0)) if isinstance(buy_result, dict) else 0
                withdraw_result = auto_withdraw(profit)
                if withdraw_result.get('status') != 'No withdrawal, profit below threshold':
                    log_compliance("WITHDRAWAL", withdraw_result)
        await self.api.close()
