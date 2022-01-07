"""
Urls for the reports app
"""
from django.urls import path

from .views import LoadBuildingDataView

urlpatterns = [
    path("load/", LoadBuildingDataView.as_view(), name="load_data"),
]
