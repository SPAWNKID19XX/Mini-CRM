from django.shortcuts import render, HttpResponse
from .models import Clients
from .form import NewCustomerForm

def get_list(request):
    customers = Clients.objects.all()
    context = {
        'title':'Clients',
        'clients': customers
    }
    return render(request, 'clients.html', context)

def add_new_customer(request):
    context = {
        'title': 'Add new customer',
        'form': NewCustomerForm()
    }
    return render(request, 'add_customer.html', context)