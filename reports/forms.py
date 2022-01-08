"""
Form for the reports app
"""
from django import forms


class CSVFileUploadForm(forms.Form):
    """
    Form to upload a csv file containing the required data
    """

    building_data = forms.FileField(
        required=False,
        help_text='Please add a csv file containing all '
                  'the building data. Format: id, name'
    )
    meter_data = forms.FileField(
        required=False,
        help_text='Please add a csv file containing the meter data '
                  'for existing buildings. '
                  'Format: building_id, id, fuel, unit'
    )
    meter_reading_data = forms.FileField(
        required=False,
        help_text='Please add a csv file containing the reading data '
                  'for existing meters. '
                  'Format: consumption, meter_id, reading_date_time'
    )
