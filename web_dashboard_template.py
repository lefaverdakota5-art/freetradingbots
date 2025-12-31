from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/customweb", tags=["CustomWebDashboard"])

@router.get("/dashboard", response_class=HTMLResponse)
def custom_dashboard():
    html = """
    <html><head><title>Custom Trading Dashboard</title></head><body>
    <h1>Customizable Trading Dashboard</h1>
    <div id='charts'>
      <h2>Charts (placeholder)</h2>
      <!-- Insert chart.js or plotly.js here -->
    </div>
    <div id='stats'>
      <h2>Stats (placeholder)</h2>
      <!-- Insert stats, balances, PnL, etc. -->
    </div>
    <div id='controls'>
      <h2>Controls (placeholder)</h2>
      <!-- Insert start/stop, strategy selection, etc. -->
    </div>
    </body></html>
    """
    return HTMLResponse(content=html)
