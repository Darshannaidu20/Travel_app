from django_filters import rest_framework as filters
from .models import Destination
import os


class DestinationFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    country = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    best_time_to_visit = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(lookup_expr='icontains')
    image_url = filters.CharFilter(method='filter_image_url')
    created_at = filters.DateFilter(field_name='created_at', lookup_expr='date')
    updated_at= filters.DateFilter(field_name='created_at', lookup_expr='date')
    creator__username = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Destination
        fields = ['name', 'country', 'description', 'best_time_to_visit', 'category', 'image_url', 'created_at','updated_at']

   

