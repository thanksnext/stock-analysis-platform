from django.db import models


class HolidayManager(models.Manager):
    def create_holiday(
        self,
        date,
    ):
        holiday = self.create(
            date=date,
        )
        return holiday


class Holiday(models.Model):

    date = models.DateField(help_text="date", null=True)

    objects = HolidayManager()

    def __str__(self):
        return f"{self.date}"

    class Meta:
        db_table = "holiday"
