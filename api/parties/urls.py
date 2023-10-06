from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from parties import views

urlpatterns = [
    path(
        "parties/",
        views.PartyList.as_view(),
        name="party-list",
    ),
    path(
        "parties/<int:pk>/",
        views.PartyDetail.as_view(),
        name="party-detail",
    ),
    path(
        "parties/admissions/",
        views.AdmissionList.as_view(),
        name="admission-list",
    ),
    path(
        "parties/admissions/<int:pk>/",
        views.AdmissionDetail.as_view(),
        name="admission-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
