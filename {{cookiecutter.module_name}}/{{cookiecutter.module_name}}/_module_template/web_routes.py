from fastapi import APIRouter, Request

from ... import container as container
from genogrow.config.settings import templates

router = APIRouter(prefix="/{module_name}")


@router.get("")
async def get(request: Request):
    return templates.TemplateResponse(
        name="{module_name}/index.html", context={"request": request}
    )
