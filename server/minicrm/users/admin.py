from django.contrib import admin
from .models import MyUsers


class MyUsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.register(MyUsers, MyUsersAdmin)
