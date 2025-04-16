from django.urls import path
from .views import AppUserListView, AppUserFullListView

urlpatterns = [
    path('users/', AppUserListView.as_view(), name='user-list'),
    path('users-full/', AppUserFullListView.as_view(), name='user-full-list'),
]
