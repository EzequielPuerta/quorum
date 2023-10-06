from datetime import date, datetime

import pytest

from districts.models import District
from districts.tests.conftest import *  # noqa
from parties.models import Admission, Party


@pytest.fixture
def default_party_name() -> str:
    yield "Fake Party"


@pytest.fixture
def default_date() -> date:
    yield datetime.strptime("06/10/2023", "%d/%m/%Y").date()


@pytest.fixture
def default_district_number() -> int:
    yield 10


@pytest.fixture
def persisted_party(default_party_name) -> Party:
    yield Party.objects.create(name=default_party_name)


@pytest.fixture
def persisted_admission(
    default_district_number: int,
    persisted_party: Party,
    default_date: date,
    persisted_district: District,
) -> Admission:
    yield Admission.objects.create(
        district_number=default_district_number,
        district=persisted_district,
        party=persisted_party,
        date=default_date,
    )
