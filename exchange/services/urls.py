from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<int:serviceid>/', service_by_id)
]