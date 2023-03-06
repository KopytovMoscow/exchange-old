from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:orderid>/', order_by_id),
    path('add/', add_order, name='add_order'),
]