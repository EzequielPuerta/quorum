import pytest
from django.db.utils import IntegrityError

from districts.models import District


def test_district_creation() -> None:
    district = District(
        name=District.NATIONAL,
        is_national=True,
    )
    assert district.name == District.NATIONAL
    assert district.is_national


def test_national_district_representation() -> None:
    district = District(
        name=District.NATIONAL,
        is_national=True,
    )
    assert str(district) == f"{District.NATIONAL} | NATIONAL"


def test_no_national_district_representation(
    default_district_name: str,
) -> None:
    district = District(
        name=default_district_name,
        is_national=False,
    )
    assert str(district) == default_district_name


@pytest.mark.django_db
def test_district_persisted_creation(
    persisted_district: District,
    default_district_name: str,
) -> None:
    assert persisted_district.id is not None
    assert persisted_district.name == default_district_name
    assert not persisted_district.is_national


@pytest.mark.django_db
def test_district_unique(
    persisted_district: District,
    default_district_name: str,
) -> None:
    assert persisted_district.id is not None
    with pytest.raises(IntegrityError):
        District.objects.create(
            name=default_district_name,
            is_national=False,
        )


@pytest.mark.django_db
def test_district_equality(persisted_district: District) -> None:
    assert [persisted_district] == [persisted_district]
    assert {"1": persisted_district} == {"1": persisted_district}
