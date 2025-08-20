from django.shortcuts import render, HttpResponse, redirect
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
    }
    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            print("Form is valid, saving data...")
            cd = form.cleaned_data
            print("Cleaned data:", cd)
            new_client = Clients(
                name=cd['name'],
                email=cd['email'],
                phone=cd['phone']
            )
            new_client.save()
            print("New client saved:", new_client)
            context['success_msg'] = "New customer added successfully!"
            context['form'] = NewCustomerForm() 
            return redirect('get_list')
        else:
            context['form'] = form  
    else:
        context['form'] = NewCustomerForm()
    return render(request, 'add_customer.html', context)
