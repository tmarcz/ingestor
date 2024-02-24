import pytest
from fastapi.testclient import TestClient
import tests.setup
import src.config as config

import src.app.router as r

client = TestClient(r.router)


def test_http_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == 'pong!'

