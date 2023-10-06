import pytest

from districts.models import District
from districts.serializers import DistrictSerializer


@pytest.mark.django_db
def test_district_serializer_for_instance(
    default_district_name: str,
    persisted_district: District,
) -> None:
    serializer = DistrictSerializer(
        instance=persisted_district,
        context={"request": None},
    )

    _id = persisted_district.id
    assert serializer.data["id"] == _id
    assert serializer.data["url"] == f"/districts/{_id}/"
    assert serializer.data["name"] == persisted_district.name
    assert serializer.data["is_national"] == persisted_district.is_national


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
