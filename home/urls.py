from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
