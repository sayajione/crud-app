import src.healthcheck
from src import healthcheck
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(src.healthcheck.router)


# def start():
#     """Launched with `poetry run start` at root level"""
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
