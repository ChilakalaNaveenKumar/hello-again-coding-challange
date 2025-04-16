from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import AppUser, OptimizedAppUser
from .serializers import AppUserSerializer, OptimizedAppUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import AppUserFilter, OptimizedAppUserFilter

class AppUserListView(ListAPIView):
    queryset = AppUser.objects.select_related('address').all()
    serializer_class = AppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    
    filterset_class = AppUserFilter
    ordering_fields = [
        'id', 'first_name', 'last_name', 'customer_id',
        'birthday', 'created', 'last_updated',
        'address__city', 'address__country',
        'customerrelationship__points', 'customerrelationship__last_activity',
    ]
    ordering = ['id']
    
    
class OptimizedPagination(PageNumberPagination):
    page_size = 50

class OptimizedAppUserListView(ListAPIView):
    queryset = OptimizedAppUser.objects.select_related('address') \
        .prefetch_related('customerrelationship') \
        .only('id', 'customer_id', 'first_name', 'last_name', 'gender', 'birthday', 'address__country',  'address__city', 'customerrelationship__points')

    serializer_class = OptimizedAppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = OptimizedAppUserFilter
    ordering_fields = [
        'id', 'first_name', 'last_name', 'customer_id',
        'birthday', 'created', 'last_updated',
        'address__city', 'address__country',
        'customerrelationship__points', 'customerrelationship__last_activity',
    ]
    ordering = ['id']
    pagination_class = OptimizedPagination
