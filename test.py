from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.testclient import TestClient
import pytest

from main import app, users

client = TestClient(app)

@pytest.mark.parametrize("user_id, expected_status, expected_response", [
    (2, 200, {"data": users[2]}),
    (999, 404, {"detail": "User not found"})
])
def test_get_user(user_id, expected_status, expected_response):
    response = client.get(f"/api/user/{user_id}")
    assert response.status_code == expected_status
    assert response.json() == expected_response
