from django.shortcuts import render, redirect, get_object_or_404
from .models import Clients
from .form import NewCustomerForm 

def get_list(request):
    customers = Clients.objects.all()
    return render(request, 'clients.html', {
        'title': 'Clients',
        'clients': customers
    })

def add_new_customer(request):
    if request.method == 'POST':
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_list')
    else:
        form = NewCustomerForm()

    context = {
        'title': 'Add new customer',
        'form_button': 'Add Customer',
        'form': form,
        'mode': 'create',
    }

    return render(request, 'add_customer.html', context )

def edit_customer(request, pk):
    custmer = get_object_or_404(Clients, pk=pk)
    if request.method == 'POST':
        form = NewCustomerForm(request.POST, instance=custmer)
        if form.is_valid():
            form.save()
            return redirect('get_list')
    else:
        form = NewCustomerForm(instance=custmer)
    context = {
        'title': 'Update customer',
        'form_button': 'Edit Customer',
        'form': form,
        'mode': 'create',
        'customer': custmer,
    }
    return render(request, 'update_customer.html', context )


def delete_customer(request, pk):
    custmer = get_object_or_404(Clients, pk=pk)
    custmer.delete()
    return redirect('get_list')
    