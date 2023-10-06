import pytest
from rest_framework.test import APIClient

from districts.models import NATIONAL, District


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


@pytest.mark.django_db
def test_get_one_district():
    _id = 1
    client = APIClient()
    response = client.get(f"/districts/{_id}/")
    assert response.status_code == 200

    district = District.objects.get(id=_id)
    assert response.data["id"] == district.id
    assert response.data["url"] == f"http://testserver/districts/{_id}/"
    assert response.data["name"] == district.name
    assert response.data["is_national"] == district.is_national
