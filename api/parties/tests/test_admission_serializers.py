from datetime import datetime

import pytest

from districts.models import District
from parties.models import Admission, Party
from parties.serializers import AdmissionSerializer


@pytest.mark.django_db
def test_admission_serializer_for_instance(
    persisted_admission: Admission,
    persisted_district: District,
    persisted_party: Party,
) -> None:
    serializer = AdmissionSerializer(
        instance=persisted_admission,
        context={"request": None},
    )

    _id = persisted_admission.id
    assert serializer.data["id"] == _id
    assert serializer.data["url"] == f"/parties/admissions/{_id}/"
    assert (
        serializer.data["district_number"]
        == persisted_admission.district_number
    )
    assert (
        serializer.data["district"] == f"/districts/{persisted_district.id}/"
    )
    assert serializer.data["party"] == f"/parties/{persisted_party.id}/"
    assert serializer.data["date"] == datetime.strftime(
        persisted_admission.date, "%Y-%m-%d"
    )


@pytest.mark.django_db
def test_admission_serializer_for_all() -> None:
    queryset = Admission.objects.all()
    serializer = AdmissionSerializer(
        queryset,
        many=True,
        context={"request": None},
    )
    assert len(serializer.data) == 769
    admission = serializer.data[0]
    assert admission["id"] == 1
    assert admission["url"] == "/parties/admissions/1/"
    assert admission["district_number"] == 1
    assert admission["district"] == "/districts/1/"
    assert admission["party"] == "/parties/92/"
    assert admission["date"] == "1998-05-19"
