import pytest
from rest_framework.test import APIClient

from ..models import NATIONAL


@pytest.mark.django_db
def test_get_all_districts():
    client = APIClient()
    response = client.get("/districts/")
    assert response.status_code == 200
    assert len(response.data) == 25

    for district in response.data:
        _id = district["id"]
        assert district["url"] == f"http://testserver/districts/{_id}/"
        if district["name"] == NATIONAL:
            assert district["is_national"]
        else:
            assert not district["is_national"]
