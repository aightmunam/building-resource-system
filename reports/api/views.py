"""
API views for the reports app
"""
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Building, Meter
from ..selectors import (get_building_consumption_in_date_range,
                         get_chart_data_for_meter)


class MeterReadingsForDateAPIView(APIView):
    """
    Find the meter readings for a meter in a given date range
    """

    model = Meter
    queryset = Meter.objects.all()

    def get(self, request, pk):
        """
        Filter the fuel consumption of the meter based on the date range
        """
        start = request.GET.get('start')
        end = request.GET.get('end')

        filtered_readings = get_chart_data_for_meter(pk, start, end)
        return Response(filtered_readings, status=200)


class BuildingReadingsForDateAPIView(APIView):
    """
    Find the total consumption of resources by a building in the given date range
    """

    model = Building
    queryset = Building.objects.all()

    def get(self, request, pk):
        """
        Filter the building fuel consumption based on the date range
        """
        start = request.GET.get('start')
        end = request.GET.get('end')

        filtered_readings = get_building_consumption_in_date_range(pk, start, end)
        return Response(filtered_readings, status=200)
