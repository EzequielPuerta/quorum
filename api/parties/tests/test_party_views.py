import pytest
from rest_framework.test import APIClient

from parties.models import Party


@pytest.mark.django_db
def test_get_all_parties():
    client = APIClient()
    response = client.get("/parties/")
    assert response.status_code == 200
    assert len(response.data) == 269

    for party in response.data:
        _id = party["id"]
        assert party["url"] == f"http://testserver/parties/{_id}/"
        assert isinstance(party["name"], str)


@pytest.mark.django_db
def test_get_one_party():
    _id = 1
    client = APIClient()
    response = client.get(f"/parties/{_id}/")
    assert response.status_code == 200

    party = Party.objects.get(id=_id)
    assert response.data["id"] == party.id
    assert response.data["url"] == f"http://testserver/parties/{_id}/"
    assert response.data["name"] == party.name
