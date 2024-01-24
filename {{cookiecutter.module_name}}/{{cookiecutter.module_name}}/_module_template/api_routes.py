from fastapi import APIRouter

from ... import container as container

router = APIRouter(prefix="/{module_name}", tags=["{module_name}"])


@router.get("")
async def get():
    return {"{module_name}": "{module_name} works"}
