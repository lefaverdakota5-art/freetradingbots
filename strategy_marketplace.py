from fastapi import APIRouter, UploadFile, File
from pathlib import Path

router = APIRouter(prefix="/marketplace", tags=["Marketplace"])
STRATEGY_DIR = Path(__file__).parent / "strategies"
STRATEGY_DIR.mkdir(exist_ok=True)

@router.post("/upload")
def upload_strategy(file: UploadFile = File(...)):
    file_path = STRATEGY_DIR / file.filename
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"status": "uploaded", "filename": file.filename}

@router.get("")
def list_strategies():
    return [f.name for f in STRATEGY_DIR.glob("*.py")]
