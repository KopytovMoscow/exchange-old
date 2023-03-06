from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


def index(request):
    posts = Order.objects.all()
    print(posts)
    return render(request, 'orders/index.html', {'title': 'Все заказы', 'orders': posts})


def order_by_id(request, orderid):
    return render(request, 'orders/order.html', {'order_id': orderid, 'title': 'Информация о заказе'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(":(")


def add_order(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddOrderForm()
    return render(request, 'orders/add.html', {'title': 'Добавление нового заказа',
                                                'form': form})


# class RegisterUser(DataMixin, CreateView):