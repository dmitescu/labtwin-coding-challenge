import pytest
from Endpoint import app

@pytest.fixture
def client():
    return app.test_client()

def test_response(client):
    r = client.post("/process")
    assert b'processed' in r.data
