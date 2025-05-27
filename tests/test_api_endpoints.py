import pytest
import requests
from jsonschema import validate

BASE = "https://jsonplaceholder.typicode.com"

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id":     {"type": "integer"},
        "title":  {"type": "string"},
        "body":   {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"]
}

def test_get_posts_list():
    resp = requests.get(f"{BASE}/posts")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list) and len(data) > 0
    validate(instance=data[0], schema=POST_SCHEMA)

def test_get_single_post():
    resp = requests.get(f"{BASE}/posts/1")
    assert resp.status_code == 200
    post = resp.json()
    assert post["id"] == 1
    validate(instance=post, schema=POST_SCHEMA)

@pytest.mark.parametrize("post_id", [-1, 0, 9999])
def test_get_invalid_post(post_id):
    resp = requests.get(f"{BASE}/posts/{post_id}")

    assert resp.status_code in (200, 404)

def test_create_post():
    payload = {"userId": 10, "title": "foo", "body": "bar"}
    resp = requests.post(f"{BASE}/posts", json=payload)
    assert resp.status_code == 201
    created = resp.json()
    assert created["userId"] == 10
    assert "id" in created
    validate(instance=created, schema=POST_SCHEMA)
