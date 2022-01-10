"""
Urls for the reports app
"""
from django.urls import path

from .views import (BuildingDetailView, BuildingListView, FileUploadFormView,
                    IndexRedirectView, MeterDetailView)

urlpatterns = [
    path('', IndexRedirectView.as_view(), name='index'),
    path('upload/', FileUploadFormView.as_view(), name='upload_data'),
    path('buildings/', BuildingListView.as_view(), name='building_list'),
    path('meter/<int:pk>/', MeterDetailView.as_view(), name='meter_detail'),
    path('building/<int:pk>/', BuildingDetailView.as_view(), name='building_detail'),
]
