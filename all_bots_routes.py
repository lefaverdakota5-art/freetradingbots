from fastapi import APIRouter, HTTPException, BackgroundTasks
from pathlib import Path
from execute_all import run_all_bots
import asyncio

router = APIRouter(prefix="/all-bots", tags=["AllBots"])

@router.post("/run")
def run_all(app_id: str, token: str, background_tasks: BackgroundTasks):
    def runner():
        asyncio.run(run_all_bots(app_id, token))
    background_tasks.add_task(runner)
    return {"status": "started", "detail": "All bots are running in background."}
