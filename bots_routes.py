from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from typing import List

router = APIRouter(prefix="/bots", tags=["Bots"])
_BOTS_DIR = Path(__file__).resolve().parent / "bots"

def _safe_bot_path(name: str) -> Path:
    if "/" in name or "\\" in name or name.startswith("."):
        raise HTTPException(status_code=400, detail="Invalid bot name")
    p = (_BOTS_DIR / name).resolve()
    if _BOTS_DIR not in p.parents:
        raise HTTPException(status_code=400, detail="Invalid bot name")
    return p

@router.get("", response_model=List[str])
def list_bots() -> List[str]:
    if not _BOTS_DIR.exists():
        return []
    return sorted([p.name for p in _BOTS_DIR.glob("*.xml") if p.is_file()])

@router.get("/{name}")
def download_bot(name: str):
    p = _safe_bot_path(name)
    if not p.exists() or not p.is_file() or p.suffix.lower() != ".xml":
        raise HTTPException(status_code=404, detail="Bot not found")
    return FileResponse(path=str(p), media_type="application/xml", filename=p.name)
