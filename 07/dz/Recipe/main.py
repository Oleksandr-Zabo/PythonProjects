import logging

import uvicorn
from fastapi import FastAPI

try:
    from .logger_config import setup_logger
    from .router import router as recipe_router
except ImportError:
    from logger_config import setup_logger
    from router import router as recipe_router

setup_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Recipe API",
    description="CRUD API for recipes with OpenAPI documentation",
    version="1.0.0",
)
app.include_router(recipe_router)
logger.info("Recipe API initialized")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
