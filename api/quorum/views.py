from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):  # type: ignore
    return Response(
        {
            "districts": reverse(
                "district-list",
                request=request,
                format=format,
            ),
            "parties": reverse(
                "party-list",
                request=request,
                format=format,
            ),
            "admissions": reverse(
                "admission-list",
                request=request,
                format=format,
            ),
        }
    )
