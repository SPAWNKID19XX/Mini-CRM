from django.shortcuts import render
from .forms import LoginUserForm



# Create your views here.
def login(request):
    context = {
        'form': LoginUserForm(),
        'title': 'Login'
    }
    return render(request, 'login.html', context)
