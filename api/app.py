from fastapi import FastAPI

from .routes import main_router


app = FastAPI(
    title="Presentation API",
    version="0.1.0",
    description="Presenting myself",
)

app.include_router(main_router)
