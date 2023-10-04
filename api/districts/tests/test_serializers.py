import pytest

from ..models import District
from ..serializers import DistrictSerializer


@pytest.mark.django_db
def test_district_serializer_for_instance(default_district_name) -> None:
    district = District.objects.create(
        name=default_district_name,
        is_national=False,
    )

    serializer = DistrictSerializer(
        instance=district,
        context={"request": None},
    )

    _id = district.id
    assert serializer.data["id"] == district.id
    assert serializer.data["url"] == f"/districts/{_id}/"
    assert serializer.data["name"] == district.name
    assert serializer.data["is_national"] == district.is_national


@pytest.mark.django_db
def test_district_serializer_for_all() -> None:
    queryset = District.objects.all()
    serializer = DistrictSerializer(
        queryset,
        many=True,
        context={"request": None},
    )
    assert len(serializer.data) == 25
    district = serializer.data[24]
    assert district["id"] == 25
    assert district["url"] == "/districts/25/"
    assert district["name"] == District.NATIONAL
    assert district["is_national"]
