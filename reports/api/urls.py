"""
Urls for the reports api
"""
from django.urls import path

from .views import BuildingReadingsForDateAPIView, MeterReadingsForDateAPIView

urlpatterns = [
    path('building_readings/<int:pk>/', BuildingReadingsForDateAPIView.as_view(), name='building_readings'),
    path('meter_readings/<int:pk>/', MeterReadingsForDateAPIView.as_view(), name='meter_readings'),

]
