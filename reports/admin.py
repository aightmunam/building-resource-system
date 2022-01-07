"""
Admin for the reports app
"""
from django.contrib import admin

from .models import Building, Fuel, Meter, MeterReading


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ("building", "fuel", "unit")


@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ("meter", "value", "reading_taken_at")
