import logging

from fastapi import FastAPI

from app import __version__
from app.api.health import router as health_router
from app.config import get_settings
from app.logging_config import configure_logging

logger = logging.getLogger("odin.main")


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    # Documentação interativa só em modo debug (menos superfície exposta).
    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        docs_url="/docs" if settings.debug else None,
        redoc_url=None,
        openapi_url="/openapi.json" if settings.debug else None,
    )
    app.include_router(health_router, prefix="/api/v1")
    logger.info("app created (env=%s)", settings.environment)
    return app


app = create_app()
