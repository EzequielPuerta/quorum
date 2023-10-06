from django.contrib.admin import ModelAdmin, register

from parties.models import Admission, Party


@register(Party)
class PartyAdmin(ModelAdmin):
    list_display = ("id", "name", "districts")
    search_fields = ("id", "name", "admissions__district__name")
    list_filter = ("admissions__district__name",)

    def districts(self, party: Party) -> str:
        admissions = party.admissions.all()
        districts = map(lambda admission: admission.district.name, admissions)
        return ", ".join(districts)

    districts.short_description = "Districts"  # type: ignore
    districts.admin_order_field = "admissions__district__name"  # type: ignore


@register(Admission)
class AdmissionAdmin(ModelAdmin):
    list_display = ("id", "date", "party", "district_name", "district_number")
    search_fields = (
        "id",
        "date",
        "party__name",
        "district__name",
        "district_number",
    )
    list_filter = ("date", "party__name")

    def district_name(self, admission: Admission) -> str:
        return admission.district.name

    district_name.admin_order_field = "district__name"  # type: ignore
