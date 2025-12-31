from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from supabase_client import supabase

router = APIRouter(prefix="/web", tags=["WebDashboard"])

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    trades = supabase.table("trades").select("*").execute().data
    balances = supabase.table("balances").select("*").execute().data
    html = """
    <html><head><title>Trading Dashboard</title></head><body>
    <h1>Ultimate Trading Dashboard</h1>
    <h2>Balances</h2><ul>
    """
    for b in balances:
        html += f"<li>{b['asset']}: {b['balance']}</li>"
    html += "</ul><h2>Recent Trades</h2><ul>"
    for t in trades[-10:]:
        html += f"<li>{t['symbol']} {t['contract_type']} {t['amount']} result: {t['result']}</li>"
    html += "</ul></body></html>"
    return HTMLResponse(content=html)
