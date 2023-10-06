import pytest

from districts.models import District


@pytest.fixture
def default_district_name() -> str:
    yield "Fake District"


@pytest.fixture
def persisted_district(default_district_name) -> District:
    yield District.objects.create(
        name=default_district_name,
        is_national=False,
    )
