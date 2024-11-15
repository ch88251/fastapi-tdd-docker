import json
import pytest

def test_create_summary(test_app_with_db):
  response = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://test.io"}))
  assert response.status_code == 201
  assert response.json()["url"] == "https://test.io"

def test_create_summaries_invalid_json(test_app):
  response = test_app.post("/summaries", data=json.dumps({}))
  assert response.status_code == 422
  assert response.json() == {
    "detail": [
      {'loc': ['body', 'url'], 'msg': 'field required', 'type': 'value_error.missing'}
    ]
  }
