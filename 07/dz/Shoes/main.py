import logging

import uvicorn
from fastapi import FastAPI

try:
    from .router import router as shoes_router
except ImportError:
    from router import router as shoes_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Shoes API",
    description="CRUD API for shoes with OpenAPI documentation",
    version="1.0.0",
)
app.include_router(shoes_router)
logger.info("Shoes API initialized")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
