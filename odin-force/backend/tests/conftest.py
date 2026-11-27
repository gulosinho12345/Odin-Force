import pytest
from fastapi.testclient import TestClient

from app.config import get_settings
from app.main import create_app


@pytest.fixture
def client(monkeypatch):
    # Variáveis de ambiente têm prioridade sobre o .env do desenvolvedor.
    monkeypatch.setenv("ODIN_ENVIRONMENT", "test")
    monkeypatch.setenv("ODIN_DEBUG", "false")
    get_settings.cache_clear()
    with TestClient(create_app()) as c:
        yield c
    get_settings.cache_clear()
