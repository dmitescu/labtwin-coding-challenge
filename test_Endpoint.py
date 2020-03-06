import pytest
from Endpoint import app

import json

TEST_BODY = "I am a cat. I sometimes meow and purr. Other times I scratch."
TEST_SUMMARY = "I am a cat. Other times I scratch."

@pytest.fixture
def client():
    return app.test_client()

def test_wrong_ct(client):
    r = client.post("/process")
    assert r.status_code == 400

def test_processed(client):
    r = client.post(
        "/process",
        data=json.dumps({"body": TEST_BODY}),
        content_type="application/json")
    json_body = json.loads(r.data)
    assert r.status_code == 200
    assert "summary" in json_body.keys()
    assert json_body["summary"] == TEST_SUMMARY
