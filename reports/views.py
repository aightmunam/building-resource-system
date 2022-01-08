"""
Views for reports app
"""
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, ListView

from .forms import CSVFileUploadForm
from .models import Building
from .services import (
    load_buildings_from_file,
    load_meter_readings_from_file,
    load_meters_from_file
)


class FileUploadFormView(FormView):
    """
    View to allow csv files to be uploaded and load their data
    into the db
    """

    form_class = CSVFileUploadForm
    template_name = 'reports/upload.html'

    def form_valid(self, form):
        """
        If the form is valid, the added csv files are used to load data
        """
        building_file = form.cleaned_data['building_data']
        meter_file = form.cleaned_data['meter_data']
        reading_file = form.cleaned_data['meter_reading_data']

        success_message = ''

        if building_file:
            number_of_buildings_added = load_buildings_from_file(building_file)
            success_message += f'{number_of_buildings_added} buildings added from {building_file.name}. '

        if meter_file:
            number_of_meters_added = load_meters_from_file(meter_file)
            success_message += f'{number_of_meters_added} meters added from {meter_file.name}. '

        if reading_file:
            number_of_readings_added = load_meter_readings_from_file(reading_file)
            success_message += f'{number_of_readings_added} meter readings added from {reading_file.name}. '

        context = self.get_context_data()
        context['message'] = 'Data successfully loaded. ' + success_message
        context['redirect_url'] = reverse('upload_data')

        return render(self.request, 'success.html', context)


class BuildingListView(ListView):
    """
    Display a list of all the buildings
    """

    template_name = 'reports/list.html'
    paginate_by = 5
    context_object_name = 'buildings'
    model = Building
