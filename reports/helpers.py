"""
All the helpers for the reports app
"""
import csv


def parse_data_from_file(file):
    """
    Parse the csv file and return all the non-empty rows

    Args:
        file (str): Csv file to get the data from

    Returns:
        list: A list of lists where each of them contains the
        data to be added into the database
    """
    objects = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if any(row):
                objects.append(row)

    return objects
