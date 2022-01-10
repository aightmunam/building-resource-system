"""
All the models for the reports app
"""
from django.db import models
from django.db.models import Sum


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

    @property
    def building_meters(self):
        """
        Get all the meters associated with the building and
        cache the fuel as well
        """
        return self.meters.all().select_related('fuel').order_by('id')


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

    @property
    def total_consumption(self):
        """
        Total consumption made by the meter
        """
        return sum(self.readings.values_list('value', flat=True))


class MeterReadingQuerySet(models.QuerySet):

    def annotate_daily_consumption(self):
        """
        Add the daily consumption of the meter readings
        """
        return self.values('reading_taken_at__date').annotate(total_daily_consumption=Sum('value'))


class MeterReading(TimeStampMixin):
    """
    Model to represent the reading of a meter
    """

    meter = models.ForeignKey(
        "reports.Meter", related_name="readings", on_delete=models.CASCADE
    )
    value = models.FloatField()
    reading_taken_at = models.DateTimeField()

    objects = MeterReadingQuerySet.as_manager()

    class Meta:
        verbose_name = "MeterReading"
        verbose_name_plural = "MeterReadings"

    def __str__(self):
        return f"Meter: {self.meter_id}, value: {self.value}, time: {self.reading_taken_at}"
