from fastapi import FastAPI, BackgroundTasks, HTTPException
from bots_routes import router as bots_router
from all_bots_routes import router as all_bots_router
from dashboard import router as dashboard_router
from strategy_marketplace import router as marketplace_router
from web_dashboard import router as web_dashboard_router
from web_dashboard_template import router as custom_web_dashboard_router
from bot_executor import BotExecutor
from pathlib import Path
import asyncio



app = FastAPI()
app.include_router(bots_router)
app.include_router(all_bots_router)
app.include_router(dashboard_router)
app.include_router(marketplace_router)
app.include_router(web_dashboard_router)
app.include_router(custom_web_dashboard_router)

running_bots = {}

@app.post("/run-bot/{bot_name}")
def run_bot(bot_name: str, app_id: str, token: str, background_tasks: BackgroundTasks):
    bot_path = Path(__file__).parent / "bots" / bot_name
    if not bot_path.exists():
        raise HTTPException(status_code=404, detail="Bot not found")
    executor = BotExecutor(str(bot_path), app_id, token)
    task = asyncio.create_task(executor.run())
    running_bots[bot_name] = task
    return {"status": "started", "bot": bot_name}

@app.post("/stop-bot/{bot_name}")
def stop_bot(bot_name: str):
    task = running_bots.get(bot_name)
    if task:
        task.cancel()
        return {"status": "stopped", "bot": bot_name}
    return {"status": "not running", "bot": bot_name}
