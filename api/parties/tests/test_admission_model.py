from datetime import date

import pytest

from districts.models import District
from parties.models import Admission, Party


def test_admission_creation(
    default_date: date,
    default_party_name: str,
    default_district_number: int,
    default_district_name: str,
) -> None:
    party = Party(name=default_party_name)
    district = District(
        name=default_district_name,
        is_national=False,
    )
    admission = Admission(
        district_number=default_district_number,
        district=district,
        party=party,
        date=default_date,
    )
    assert admission.district_number == default_district_number
    assert admission.district == district
    assert admission.party == party
    assert admission.date == default_date


def test_admission_representation(
    default_date: date,
    default_party_name: str,
    default_district_number: int,
    default_district_name: str,
) -> None:
    party = Party(name=default_party_name)
    district = District(
        name=default_district_name,
        is_national=False,
    )
    admission = Admission(
        district_number=default_district_number,
        district=district,
        party=party,
        date=default_date,
    )
    assert str(admission) == f"{default_party_name} ({default_district_name})"


@pytest.mark.django_db
def test_admission_persisted_creation(
    persisted_admission: Admission,
    default_district_number: int,
    persisted_party: Party,
    default_date: date,
    persisted_district: District,
) -> None:
    assert persisted_admission.id is not None
    assert persisted_admission.district_number == default_district_number
    assert persisted_admission.district == persisted_district
    assert persisted_admission.party == persisted_party
    assert persisted_admission.date == default_date


@pytest.mark.django_db
def test_admission_equality(
    persisted_admission: Admission,
) -> None:
    assert [persisted_admission] == [persisted_admission]
    assert {"1": persisted_admission} == {"1": persisted_admission}
