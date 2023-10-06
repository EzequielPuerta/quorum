from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    IntegerField,
    Model,
)

from districts.models import District


class Party(Model):
    name = CharField(max_length=256, help_text="Party name", unique=True)

    class Meta:
        ordering = ("name", "id")
        verbose_name = "party"
        verbose_name_plural = "parties"

    def __str__(self) -> str:
        return self.name


class Admission(Model):
    district_number = IntegerField()
    district = ForeignKey(
        District,
        related_name="admissions",
        on_delete=CASCADE,
    )
    party = ForeignKey(
        Party,
        related_name="admissions",
        on_delete=CASCADE,
    )
    date = DateField(null=True)

    class Meta:
        ordering = ("-date", "district", "party", "district_number")

    def __str__(self) -> str:
        return f"{self.party.name} ({self.district.name})"
