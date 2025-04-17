from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Subquery, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import AppUser, OptimizedAppUser, OptimizedCustomerRelationship
from .serializers import AppUserSerializer, OptimizedAppUserSerializer
from .filters import AppUserFilter, OptimizedAppUserFilter


class Pagination(PageNumberPagination):
    page_size = 50


class AppUserListView(ListAPIView):
    queryset = AppUser.objects.select_related('address').prefetch_related('customerrelationships').all()
    serializer_class = AppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AppUserFilter
    ordering_fields = [
        'id', 'first_name', 'last_name', 'customer_id',
        'birthday', 'created', 'last_updated',
        'address__city', 'address__country',
        'customerrelationships__points', 'customerrelationships__last_activity',
    ]
    ordering = ['id']
    pagination_class = Pagination
class OptimizedAppUserListView(ListAPIView):
    queryset = OptimizedAppUser.objects.annotate(
        points=Subquery(
            OptimizedCustomerRelationship.objects.filter(
                appuser=OuterRef('pk')
            ).values('points')[:1]
        )
    ).select_related('address').prefetch_related('customerrelationships').all()
    serializer_class = OptimizedAppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OptimizedAppUserFilter
    ordering_fields = [
        'id', 'first_name', 'last_name', 'customer_id',
        'birthday', 'created', 'last_updated',
        'address__city', 'address__country',
        'customerrelationships__points', 'customerrelationships__last_activity',
    ]
    ordering = ['id']
    pagination_class = Pagination
