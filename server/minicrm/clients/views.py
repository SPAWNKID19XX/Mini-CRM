from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Clients
from .form import NewCustomerForm 
from django.contrib import messages

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
            messages.success(request, 'New customer added successfully.')
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
    
    try:
        customer = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        messages.error(request, 'Customer not found.')
        return redirect('get_list')
    print(customer)     
    print(pk)
    print(messages)
    
    if request.method == 'POST':
        form = NewCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully.')
            return redirect('get_list')
    else:
        form = NewCustomerForm(instance=customer)
    context = {
        'title': 'Update customer',
        'form_button': 'Edit Customer',
        'form': form,
        'mode': 'create',
        'customer': customer,
    }
    return render(request, 'update_customer.html', context )


def delete_customer(request, pk):
    custmer = get_object_or_404(Clients, pk=pk)
    custmer.delete()
    messages.success(request, 'Customer deleted successfully.')
    return redirect('get_list')
    