from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from districts import views

urlpatterns = [
    path(
        "districts/",
        views.DistrictList.as_view(),
        name="district-list",
    ),
    path(
        "districts/<int:pk>/",
        views.DistrictDetail.as_view(),
        name="district-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
