from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Orders

def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def template(request):
    title = 'Country: {0}; City: {1}'.format('Belarus', 'Mogilew')
    times = [ 1, 2, 3, 4, 5 ]
    content = { 
        'firstName': 'Tomas', 
        'lastName': 'Tester', 
        'title': title, 
        'times': times 
    }
    return render(request, 'example-template.html', content)

def store(request): 
    orders = Orders.objects.all()
    sortOrders = Orders.objects.order_by('_id')
    print(orders)
    return orders