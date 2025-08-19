from django.shortcuts import render, HttpResponse
from .models import Clients

def get_list(request):
    customers = Clients.objects.all()
    context = {
        'title':'Clients',
        'clients': customers
    }
    return render(request, 'clients.html', context)