from rest_framework import serializers

from parties.models import Admission, Party


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = (
            "id",
            "url",
            "name",
        )


class AdmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admission
        fields = (
            "id",
            "url",
            "district_number",
            "district",
            "party",
            "date",
        )
