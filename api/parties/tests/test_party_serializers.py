import pytest

from parties.models import Party
from parties.serializers import PartySerializer


@pytest.mark.django_db
def test_party_serializer_for_instance(
    default_party_name: str,
    persisted_party: Party,
) -> None:
    serializer = PartySerializer(
        instance=persisted_party,
        context={"request": None},
    )

    _id = persisted_party.id
    assert serializer.data["id"] == _id
    assert serializer.data["url"] == f"/parties/{_id}/"
    assert serializer.data["name"] == persisted_party.name


@pytest.mark.django_db
def test_parties_serializer_for_all() -> None:
    queryset = Party.objects.all()
    serializer = PartySerializer(
        queryset,
        many=True,
        context={"request": None},
    )
    assert len(serializer.data) == 269
    party = serializer.data[0]
    assert party["id"] == 1
    assert party["url"] == "/parties/1/"
    assert party["name"] == "Acción Chaqueña"
