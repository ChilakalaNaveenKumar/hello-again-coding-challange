from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import AppUser
from .serializers import AppUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import AppUserFilter

class AppUserListView(ListAPIView):
    queryset = AppUser.objects.select_related('address').all()
    serializer_class = AppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    
    filterset_class = AppUserFilter
    search_fields = ['first_name', 'last_name', 'phone_number']
    ordering_fields = [
        'id', 'first_name', 'last_name', 'customer_id',
        'birthday', 'created', 'last_updated',
        'address__city', 'address__country',
        'customerrelationship__points', 'customerrelationship__last_activity',
    ]
    ordering = ['id']

class NoPagination(PageNumberPagination):
    page_size = None
class AppUserFullListView(ListAPIView):
    queryset = AppUser.objects.select_related('address').all()
    serializer_class = AppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    pagination_class = NoPagination
    
    filterset_fields = ['gender', 'birthday', 'address__city', 'customer_id']
    search_fields = ['first_name', 'last_name', 'phone_number']
    ordering_fields = '__all__'
    ordering = ['id']
