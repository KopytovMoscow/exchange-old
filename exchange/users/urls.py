from django.urls import path


from .views import *

urlpatterns = [
    path('', UsersHome.as_view()),
    # path('register/', RegisterUser.as_view(), name="register")
]