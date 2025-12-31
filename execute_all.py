import os
import asyncio
from pathlib import Path
from bot_executor import BotExecutor

BOTS_DIR = Path(__file__).parent / "bots"

async def run_all_bots(app_id, token):
    tasks = []
    for bot_file in BOTS_DIR.glob("*.xml"):
        executor = BotExecutor(str(bot_file), app_id, token)
        tasks.append(asyncio.create_task(executor.run()))
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python execute_all.py <app_id> <token>")
        sys.exit(1)
    app_id = sys.argv[1]
    token = sys.argv[2]
    asyncio.run(run_all_bots(app_id, token))
