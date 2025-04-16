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
    created = rest_framework.DateTimeFilter()
    last_updated = rest_framework.DateTimeFilter()

    # Address fields
    address__street = rest_framework.CharFilter()
    address__city = rest_framework.CharFilter()
    address__country = rest_framework.CharFilter()

    # CustomerRelationship fields
    customerrelationship__points = rest_framework.NumberFilter()
    customerrelationship__created = rest_framework.DateTimeFilter()
    customerrelationship__last_activity = rest_framework.DateTimeFilter()

    class Meta:
        model = AppUser
        fields = []