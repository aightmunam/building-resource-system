"""
Selectors to fetch data from the database
"""
import json

from django.db.models import F, Sum

from .models import Meter, MeterReading


def get_chart_data_for_meter(meter_id, start_date, end_date):
    """
    Get all the reading data for a meter and return it in json
    format that can be used in charts

    Args:
        meter_id (id): Id of the meter
        start_date (str): Start date for the readings
        end_date (str): End date for the readings

    Returns:
        json: All the meter readings for the current meter in the
        given date range
    """
    if not (start_date and end_date):
        return {}

    meter = Meter.objects.filter(id=meter_id).select_related('fuel').first()
    readings = meter.readings.filter(reading_taken_at__range=[start_date, end_date])

    chart_data = {
        'readings': list(
            readings.values(y=F('value'), x=F('reading_taken_at'))
        ),
        'label': {
            'resource': meter.fuel.name,
            'unit': meter.unit
        }
    }

    return json.dumps(chart_data, default=str)


def get_building_consumption_in_date_range(building_id, start_date, end_date):
    """
    Get all the reading data for a building and return it in json
    format that can be used in charts

    Args:
        building_id (id): Id of the building
        start_date (str): Start date for the readings
        end_date (str): End date for the readings

    Returns:
        json: All the meter readings for the current meter in the
        given date range
    """
    if not (start_date and end_date):
        return {}

    readings = MeterReading.objects.filter(
        meter__building_id=building_id,
        reading_taken_at__range=[start_date, end_date]
    )

    readings = readings.values(
        'reading_taken_at__month',
        'reading_taken_at__year',
        'reading_taken_at__hour',
    ).annotate(total_value=Sum('value'))

    filtered_readings = {
        'electricity': list(
            readings.filter(meter__fuel__name='Electricity').values(
                y=F('total_value'),
                x=F('reading_taken_at'),
            )
        ),
        'natural_gas': list(
            readings.filter(meter__fuel__name='Natural Gas').values(
                y=F('total_value'),
                x=F('reading_taken_at'),
            )
        ),
        'water': list(
            readings.filter(meter__fuel__name='Water').values(
                y=F('total_value'),
                x=F('reading_taken_at'),
            )
        ),
    }

    return json.dumps(filtered_readings, default=str)
