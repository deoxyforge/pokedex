# Main agent and launcher for the application
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)