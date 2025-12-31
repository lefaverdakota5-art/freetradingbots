# FreeTradingBots FastAPI + Supabase + Railway

## Features
- Upload and manage Deriv/Binary XML bots
- Execute all bots in parallel via API
- Supabase integration for future data storage (user data, bot runs, etc.)
- Ready for Railway deployment (Dockerfile included)

## Setup

### 1. Environment Variables
Set these in Railway (or locally in a .env file):
- `SUPABASE_URL` = your Supabase project URL
- `SUPABASE_KEY` = your Supabase service role key

### 2. Deploy to Railway
- Push this repo to GitHub
- Create a new Railway project, link your repo
- Set the environment variables above in Railway dashboard
- Deploy (Railway will use the Dockerfile)

### 3. Usage
- Place your XML bots in the `bots/` directory
- Start all bots: `POST /all-bots/run` (with app_id and token in body)
- List bots: `GET /bots`
- Download bot: `GET /bots/{name}`

## Extending
- Use `supabase_client.py` to interact with your Supabase database
- Add endpoints or logic as needed for your use case

---

For help, contact your developer or see the Railway/Supabase docs.
# freeTradingBots - Make sure to back test before using
This is a repository for free bots that you can use to trade at your own discretion and earn millions.


Trade for free using the best Bots
https://free.money8gg.com

Free Trading Bots Repository: Automate Your Trading Strategies
Description
Welcome to the Free Trading Bots Repository! This repository is your one-stop solution for all free and open-source trading bots across various platforms and languages. From cryptocurrency trading bots like Bitcoin, Ethereum, and other altcoins to traditional stock market trading, we've got you covered. Automate your trading strategies and optimize your profits without spending a dime on expensive bots.



Free Trading Bots
Crypto Trading Bots
Stock Market Trading Bots
Algorithmic Trading
Automated Trading
Forex Trading Bots
Open Source Trading
Python Trading Bot
JavaScript Trading Bot
Features
Variety of Bots: Collection of bots for Forex, Stocks, and Cryptocurrency markets.
Multi-Language Support: Bots are available in languages such as Python, JavaScript, Java, and more.
Cross-Platform: Bots that can run on various platforms like Binance, MetaTrader, Coinbase, etc.
Easy to Use: Well-documented code with setup guides for each bot.
Community Support: A community of developers and traders contributing to the project.
Table of Contents
Installation
Usage
Contributing
License
FAQs
Installation
Follow the individual README files inside each bot's folder for installation instructions.

Create an Account: 
https://money8gg.com

# Wondering how to deposit

#option 1: use Browser
- Visit [money.money8gg.com](https://money.money8gg.com/signin)
- click i don't have an account sign up
- link your deriv account
- confirm your details
- Add your phonenumber(the one you use for mpesa to receive money during withdraws and to receive prompt during deposits)
- Add your password
- You are redirected back to sign in (use your email and passwordyou added to login)
- If you want to deposit - simply click deposit on the home page
- If you want to withdraw simply press withdraw on home screen or even on side bar
- If you face any issues text me at  +254 792 673 175

# Option 2: Manual option( send the money to till then send your CR number to whatsapp) -
- Kindly send the amount you want to deposit to till 4475834 (GEIGHTFORGEIGHT INVESTMENT)
- whatsapp your cr number to +254 792 673 175
- wait 1 minute and the deposit should be done
- check your account to ensure the dollars have been credited

# WHERE TO LEARN FOR FREE
Youtube: https://www.youtube.com/channel/UCVpd8EuS8yAWMGkNtZ23Y3A

- 
Usage
Check the guide inside each bot’s directory to learn how to deploy and customize the trading bot.

Contributing
Feel free to contribute to this repository by creating a pull request or opening an issue. For detailed contributing guidelines, check out the CONTRIBUTING.md file.

License
All bots in this repository are open-source under the MIT License. See the LICENSE file for details.

FAQs
Visit our FAQs section to find answers to commonly asked questions.

Note: Trading involves risks. It's recommended to understand the risks before deploying any bot in a live trading environment.

If you find this repository useful, please star it to make it more visible to the community. Happy Trading! 📈
