from fastapi import APIRouter

from ... import container as container

router = APIRouter(prefix="/demo", tags=["demo"])


@router.get("")
async def get_demo():
    return {"demo": "demo works"}
