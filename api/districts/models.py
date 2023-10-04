from django.db.models import BooleanField, CharField, Model

NATIONAL = "Orden Nacional"


class District(Model):
    NATIONAL = NATIONAL

    name = CharField(max_length=100, help_text="District name", unique=True)
    is_national = BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}{' | NATIONAL' if self.is_national else ''}"
