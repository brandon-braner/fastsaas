from fastapi import APIRouter
import importlib
import os

web_router = APIRouter()
api_router = APIRouter()


def auto_mount_routes():
    current_folder = f"{os.getcwd()}/{{cookiecutter.module_name}}/modules"
    subfolders = [
        f
        for f in os.listdir(current_folder)
        if (os.path.isdir(os.path.join(current_folder, f)) and not f.startswith("__"))
    ]

    for folder in subfolders:
        routes = ["api", "web"]
        name = f"{{cookiecutter.module_name}}.modules.{folder}"

        for route in routes:
            path = f"{name}.{route}_routes"
            if not os.path.exists(f"{path}.py"):
                continue
            router = importlib.import_module(path)
            if route == "api":
                api_router.include_router(router.router)
            elif route == "web":
                web_router.include_router(router.router)


auto_mount_routes()
