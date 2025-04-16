from django_filters import rest_framework
from .models import AppUser

    
class AppUserFilter(rest_framework.FilterSet):
    # AppUser fields
    first_name = rest_framework.CharFilter(lookup_expr='icontains')
    last_name = rest_framework.CharFilter(lookup_expr='icontains')
    gender = rest_framework.CharFilter()
    phone_number = rest_framework.CharFilter()
    customer_id = rest_framework.CharFilter()
    birthday = rest_framework.DateFilter()
    created = rest_framework.DateFilter()
    last_updated = rest_framework.DateFilter()

    # Address fields
    address__street = rest_framework.CharFilter()
    address__city = rest_framework.CharFilter()
    address__country = rest_framework.CharFilter()

    # CustomerRelationship fields
    customerrelationship__points = rest_framework.NumberFilter()
    customerrelationship__created = rest_framework.DateFilter()
    customerrelationship__last_activity = rest_framework.DateFilter()

    class Meta:
        model = AppUser
        fields = []
        
class OptimizedAppUserFilter(rest_framework.FilterSet):
    # AppUser fields
    first_name = rest_framework.CharFilter(lookup_expr='icontains')
    last_name = rest_framework.CharFilter(lookup_expr='icontains')
    gender = rest_framework.CharFilter()
    phone_number = rest_framework.CharFilter(lookup_expr='icontains')
    customer_id = rest_framework.CharFilter(lookup_expr='icontains')
    birthday = rest_framework.DateFromToRangeFilter()
    created = rest_framework.DateFromToRangeFilter()
    last_updated = rest_framework.DateFromToRangeFilter()

    # Address fields
    address__street = rest_framework.CharFilter()
    address__city = rest_framework.CharFilter()
    address__country = rest_framework.CharFilter()

    # CustomerRelationship fields
    customerrelationship__points = rest_framework.RangeFilter()
    customerrelationship__created = rest_framework.DateFromToRangeFilter()
    customerrelationship__last_activity = rest_framework.DateFromToRangeFilter()