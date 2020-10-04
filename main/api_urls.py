from django.urls import path
from rest_framework import routers


from main.api.views.views import UsersView

urlpatterns = [
    path('users/<slug:role>/', UsersView.as_view(), name='user'),
]
