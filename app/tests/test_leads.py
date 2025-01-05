# app/tests/test_leads.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_lead():
    response = client.post("/leads/", json={"name": "Lead 1", "status": "new"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Lead 1", "status": "new", "created_at": "timestamp", "updated_at": "timestamp"}

def test_get_leads():
    response = client.get("/leads/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
