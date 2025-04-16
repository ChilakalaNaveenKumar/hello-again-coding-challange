from django.urls import path
from .views import AppUserListView

urlpatterns = [
    path('users/', AppUserListView.as_view(), name='user-list'),
]
