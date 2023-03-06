from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

# from .forms import *
from .models import *


class UsersHome(ListView):
    model = User
    template_name = 'users/index.htmls'


def index(request):
    return HttpResponse("Users page")


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     templatename = 'users/register.html'
#     success_url = reverse_lazy('login')