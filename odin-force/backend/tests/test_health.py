from app import __version__


def test_health_ok(client):
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    assert r.json() == {
        "status": "ok",
        "app": "ODIN FORCE",
        "version": __version__,
        "environment": "test",
    }


def test_health_rejects_post(client):
    assert client.post("/api/v1/health").status_code == 405


def test_unknown_route_returns_404(client):
    assert client.get("/api/v1/nao-existe").status_code == 404


def test_docs_disabled_when_not_debug(client):
    assert client.get("/docs").status_code == 404
    assert client.get("/openapi.json").status_code == 404
