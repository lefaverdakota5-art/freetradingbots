from fastapi import APIRouter
from supabase_client import supabase

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/stats")
def get_stats():
    trades = supabase.table("trades").select("*").execute().data
    balances = supabase.table("balances").select("*").execute().data
    return {"trades": trades, "balances": balances}
