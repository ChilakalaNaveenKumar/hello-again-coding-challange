from django.urls import path
from .views import AppUserListView, OptimizedAppUserListView

urlpatterns = [
    path('users/', AppUserListView.as_view(), name='user-list'),
    path('optimized-users/', OptimizedAppUserListView.as_view(), name='optimized-users'),
]
