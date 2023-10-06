from datetime import datetime

import pytest
from rest_framework.test import APIClient

from parties.models import Admission


@pytest.mark.django_db
def test_get_all_admissions():
    client = APIClient()
    response = client.get("/parties/admissions/")
    assert response.status_code == 200
    assert len(response.data) == 769

    for admission in response.data:
        _id = admission["id"]
        assert (
            admission["url"] == f"http://testserver/parties/admissions/{_id}/"
        )
        assert isinstance(admission["district_number"], int)
        assert str(admission["district"]).startswith(
            "http://testserver/districts/"
        )
        assert str(admission["party"]).startswith("http://testserver/parties/")
        if admission["date"] is not None:
            assert datetime.strptime(admission["date"], "%Y-%m-%d")


@pytest.mark.django_db
def test_get_one_admission():
    _id = 1
    client = APIClient()
    response = client.get(f"/parties/admissions/{_id}/")
    assert response.status_code == 200

    admission = Admission.objects.get(id=_id)
    assert response.data["id"] == admission.id
    assert (
        response.data["url"] == f"http://testserver/parties/admissions/{_id}/"
    )
    assert response.data["district_number"] == admission.district_number
    assert (
        response.data["district"]
        == f"http://testserver/districts/{admission.district.id}/"
    )
    assert (
        response.data["party"]
        == f"http://testserver/parties/{admission.party.id}/"
    )
    assert datetime.strptime(response.data["date"], "%Y-%m-%d")
