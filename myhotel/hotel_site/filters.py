from django_filters.rest_framework import FilterSet
from .models import *


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'name_hotel': ['exact'],
            'country': ['exact'],
            'address': ['exact'],
        }