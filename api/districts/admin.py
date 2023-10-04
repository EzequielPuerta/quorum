from django.contrib.admin import ModelAdmin, register

from .models import District


@register(District)
class DistrictAdmin(ModelAdmin):
    list_display = ("id", "name", "is_national")
