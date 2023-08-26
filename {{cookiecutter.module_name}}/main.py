from fastapi import FastAPI
import {{ cookiecutter.module_name }}.container as container


def bootstrap_app() -> FastAPI:
    """Bootstraps the FastAPI app."""
    app = FastAPI()
    container.register_providers()
    bootstrap_routes(app)
    return app


def bootstrap_routes(app: FastAPI) -> None:
    """Bootstraps the FastAPI routes."""
    import {{cookiecutter.module_name}}.modules as modules

    app.include_router(modules.web_router, tags=["web"], include_in_schema=False)
    app.include_router(modules.api_router, prefix="/api")


app = bootstrap_app()

if __name__ == "__main__":  # nosec
    import uvicorn

    app = bootstrap_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)  # nosec
