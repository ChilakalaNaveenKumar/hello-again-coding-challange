from rest_framework.generics import ListAPIView
from .models import AppUser
from .serializers import AppUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class AppUserListView(ListAPIView):
    queryset = AppUser.objects.select_related('address').all()
    serializer_class = AppUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    
    filterset_fields = ['gender', 'birthday', 'address__city', 'customer_id']
    search_fields = ['first_name', 'last_name', 'phone_number']
    ordering_fields = '__all__'
    ordering = ['id']



