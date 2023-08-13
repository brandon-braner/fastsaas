from fastapi import FastAPI
import singlepane_api.container as container

from singlepane_api.modules.okr.routes import router as okr_router


def bootstrap_app() -> FastAPI:
    """Bootstraps the FastAPI app."""
    app = FastAPI()
    container.register_providers()
    bootstrap_routes(app)
    return app


def bootstrap_routes(app: FastAPI) -> None:
    """Bootstraps the FastAPI routes."""
    app.include_router(okr_router, prefix="/okr", tags=["okr"])


app = bootstrap_app()

if __name__ == "__main__":  # nosec
    import uvicorn

    app = bootstrap_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)  # nosec
