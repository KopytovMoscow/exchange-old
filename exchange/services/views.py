from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


def index(request):
    posts = Service.objects.all()
    print(posts)
    return render(request, 'services/index.html', {'title': 'Все услуги', 'services': posts})


def service_by_id(request, serviceid):
    post = Service.objects.get(id=serviceid)
    return render(request, 'services/service.html', {'service_id': serviceid,
                                                     'title': 'Информация об услуге',
                                                     'service': post})


def pageNotFound(request, exception):
    return HttpResponseNotFound(":(")
