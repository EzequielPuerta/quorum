from rest_framework import generics

from parties.models import Admission, Party
from parties.serializers import AdmissionSerializer, PartySerializer


class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class AdmissionList(generics.ListCreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class AdmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
