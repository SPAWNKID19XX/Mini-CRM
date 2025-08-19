from django.contrib import admin
from .models import Clients

class ClientsAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'phone']
    list_display = ['name','email','created_at']
    search_fields = ['name','email']

admin.site.register(Clients, ClientsAdmin)