import os
import shutil

# remove poetry.lock
if os.path.exists("poetry.lock"):
    os.remove("poetry.lock")

# remove .git
if os.path.exists(".git"):
    shutil.rmtree(".git")

# copy .env.example to .env
if os.path.exists(".env.example"):
    shutil.copyfile(".env.example", ".env")
