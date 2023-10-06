import pytest
from django.db.utils import IntegrityError

from parties.models import Party


def test_party_creation(default_party_name: str) -> None:
    party = Party(name=default_party_name)
    assert party.name == default_party_name


def test_party_representation(default_party_name: str) -> None:
    party = Party(name=default_party_name)
    assert str(party) == default_party_name


@pytest.mark.django_db
def test_party_persisted_creation(
    persisted_party: Party,
    default_party_name: str,
) -> None:
    assert persisted_party.id is not None
    assert persisted_party.name == default_party_name


@pytest.mark.django_db
def test_party_unique(
    persisted_party: Party,
    default_party_name: str,
) -> None:
    assert persisted_party.id is not None
    with pytest.raises(IntegrityError):
        Party.objects.create(name=default_party_name)


@pytest.mark.django_db
def test_party_equality(persisted_party: Party) -> None:
    assert [persisted_party] == [persisted_party]
    assert {"1": persisted_party} == {"1": persisted_party}
