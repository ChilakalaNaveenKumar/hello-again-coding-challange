from django_filters import rest_framework
from .models import AppUser, OptimizedAppUser

class AppUserFilter(rest_framework.FilterSet):
    first_name = rest_framework.CharFilter(lookup_expr='icontains')
    last_name = rest_framework.CharFilter(lookup_expr='icontains')
    gender = rest_framework.CharFilter()
    phone_number = rest_framework.CharFilter()
    customer_id = rest_framework.CharFilter()
    birthday = rest_framework.DateFromToRangeFilter()
    created = rest_framework.DateFromToRangeFilter()
    last_updated = rest_framework.DateFromToRangeFilter()

    address__street = rest_framework.CharFilter()
    address__city = rest_framework.CharFilter()
    address__country = rest_framework.CharFilter()

    customerrelationship__points = rest_framework.RangeFilter()
    customerrelationship__created = rest_framework.DateFromToRangeFilter()
    customerrelationship__last_activity = rest_framework.DateFromToRangeFilter()

    class Meta:
        model = AppUser
        fields = '__all__'

class OptimizedAppUserFilter(rest_framework.FilterSet):
    first_name = rest_framework.CharFilter(lookup_expr='icontains')
    last_name = rest_framework.CharFilter(lookup_expr='icontains')
    gender = rest_framework.CharFilter()
    phone_number = rest_framework.CharFilter()
    customer_id = rest_framework.CharFilter()
    birthday = rest_framework.DateFromToRangeFilter()
    created = rest_framework.DateFromToRangeFilter()
    last_updated = rest_framework.DateFromToRangeFilter()

    address__street = rest_framework.CharFilter()
    address__city = rest_framework.CharFilter()
    address__country = rest_framework.CharFilter()

    customerrelationship__points = rest_framework.RangeFilter()
    customerrelationship__created = rest_framework.DateFromToRangeFilter()
    customerrelationship__last_activity = rest_framework.DateFromToRangeFilter()

    class Meta:
        model = OptimizedAppUser
        fields = '__all__'
