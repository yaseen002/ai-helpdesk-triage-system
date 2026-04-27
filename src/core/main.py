"""
Application entrypoint.
"""

from fastapi import FastAPI

from src.core.config import settings
from src.core.logger import logger

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/", tags=["Health"])
def health_check() -> dict[str, str]:
    """
    Health endpoint.

    Returns:
        dict[str, str]: status response
    """
    logger.info("Health endpoint called")

    return {
        "message": "AI Helpdesk Triage System running"
    }