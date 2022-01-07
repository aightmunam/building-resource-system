"""
Views for reports app
"""
from django.db import transaction
from django.http import HttpResponse
from django.views import View

from .helpers import parse_data_from_file
from .services import (
    load_buildings_from_file,
    load_meter_readings_from_file,
    load_meters_from_file,
)


class LoadBuildingDataView(View):
    @transaction.atomic
    def get(self, request, *args, **kwargs):
        load_buildings_from_file(
            "/Users/munammubashir/projects/energy/test_data/building_data.csv"
        )
        load_meters_from_file(
            "/Users/munammubashir/projects/energy/test_data/meter_data.csv"
        )
        load_meter_readings_from_file(
            "/Users/munammubashir/projects/energy/test_data/halfhourly_data.csv"
        )
        return HttpResponse("GET request!")
