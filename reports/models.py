"""
All the models for the reports app
"""
from django.db import models
from django.urls import reverse


class TimeStampMixin(models.Model):
    """
    Mixin to add datetime stamps for when an object is created or updated
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameMixin(models.Model):
    """
    Mixin to add name to a model
    """

    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Building(TimeStampMixin, NameMixin):
    """
    Model for a building
    """


class Fuel(TimeStampMixin, NameMixin):
    """
    Model to represent a fuel/resource type
    """



class Meter(TimeStampMixin):
    """
    Model to represent a meter containing a building, the resource it is for and
    the unit used to record its data
    """

    building = models.ForeignKey(
        "reports.Building", related_name="meters", on_delete=models.CASCADE
    )
    fuel = models.ForeignKey(
        "reports.Fuel", related_name="meters", on_delete=models.CASCADE
    )
    unit = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Meter"
        verbose_name_plural = "Meters"

    def __str__(self):
        return f"Building: {self.building_id}, Fuel: {self.fuel_id}, Unit: {self.unit}"

    def get_absolute_url(self):
        return reverse("Meter_detail", kwargs={"pk": self.pk})


class MeterReading(TimeStampMixin):
    """
    Model to represent the reading of a meter
    """

    meter = models.ForeignKey(
        "reports.Meter", related_name="readings", on_delete=models.CASCADE
    )
    value = models.FloatField()
    reading_taken_at = models.DateTimeField()

    class Meta:
        verbose_name = "MeterReading"
        verbose_name_plural = "MeterReadings"

    def __str__(self):
        return f"Meter: {self.meter_id}, value: {self.value}, time: {self.reading_taken_at}"

    def get_absolute_url(self):
        return reverse("MeterReading_detail", kwargs={"pk": self.pk})
