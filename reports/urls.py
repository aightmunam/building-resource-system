"""
Urls for the reports app
"""
from django.urls import path

from .views import BuildingListView, FileUploadFormView

urlpatterns = [
    path('upload/', FileUploadFormView.as_view(), name='upload_data'),
    path('buildings/', BuildingListView.as_view(), name='building_list')
]
