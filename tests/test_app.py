from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete(
        "/activities/Gym%20Class/unregister?email=john@mergington.edu"
    )

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Unregistered john@mergington.edu from Gym Class"

    activities = client.get("/activities").json()
    assert "john@mergington.edu" not in activities["Gym Class"]["participants"]
