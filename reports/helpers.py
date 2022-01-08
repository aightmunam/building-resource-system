"""
All the helpers for the reports app
"""
import csv
from io import StringIO


def parse_data_from_file(in_memory_file):
    """
    Parse the csv file and return all the non-empty rows

    Args:
        in_memory_file (InMemoryUploadedFile): Csv file to get
        the data from

    Returns:
        list: A list of lists where each of them contains the
        data to be added into the database
    """
    objects = []

    file = StringIO(in_memory_file.read().decode('utf-8'))
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        if any(row):
            objects.append(row)

    return objects
