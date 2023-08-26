from fastapi import APIRouter
from supabase_py import Client as SupabaseClient

import singlepane_api.container as container


router = APIRouter()


@router.get("")
async def get_all_okrs(
    supabase: SupabaseClient = container.deps.depends(SupabaseClient),
):
    user = supabase.auth.sign_in("brandon.braner@gmail.com", "cd007-01")

    a = 0


# async def get_all_okrs():
#     return {"okrs": "okrs"}
