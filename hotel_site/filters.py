from django_filters.rest_framework import FilterSet
from .models import *


class HotelFilter(FilterSet):
    class Meta:
        model = '__all__'
        fields = {
            'name_hotel': ['exact'],
            'country': ['exact'],
            'address': ['exact'],
            'active': ['exact'],
            '': ['gt', 'lt']
        }