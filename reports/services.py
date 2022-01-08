"""
All the service functions for the reports app
"""
from datetime import datetime

from django.utils.timezone import make_aware

from .helpers import parse_data_from_file
from .models import Building, Fuel, Meter, MeterReading


def load_buildings_from_file(file):
    """
    Extract the data from the csv file and create building
    objects using that data

    Args:
        file (InMemoryUploadedFile): Csv file containing
        the building data
    """
    buildings = []

    all_buildings_data = parse_data_from_file(file)
    for building_data in all_buildings_data:
        buildings.append(Building(id=building_data[0], name=building_data[1]))

    Building.objects.bulk_create(buildings, ignore_conflicts=True)
    return len(buildings)


def load_meters_from_file(file):
    """
    Extract the data from the csv file and add the meter
    information for the buildings

    Args:
        file (InMemoryUploadedFile): Csv file containing
        the meter data
    """
    meters = []
    all_meters_data = parse_data_from_file(file)

    for meter_data in all_meters_data:
        fuel, _ = Fuel.objects.get_or_create(name=meter_data[2])
        meters.append(
            Meter(
                building_id=meter_data[0],
                id=meter_data[1],
                fuel=fuel,
                unit=meter_data[3],
            )
        )

    Meter.objects.bulk_create(meters, ignore_conflicts=True)
    return len(meters)


def load_meter_readings_from_file(file):
    """
    Extract the data from the csv file and create the meter
    readings for the provided info

    Args:
        file (InMemoryUploadedFile): Csv file containing the
        meter reading data
    """
    readings = []
    all_reading_data = parse_data_from_file(file)

    for reading_data in all_reading_data:
        readings.append(
            MeterReading(
                value=reading_data[0],
                meter_id=reading_data[1],
                reading_taken_at=make_aware(datetime.fromisoformat(reading_data[2])),
            )
        )

    MeterReading.objects.bulk_create(readings, ignore_conflicts=True)
    return len(readings)
