from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Users.models import *
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username','email', 'name', 'last_name','gender','dni','nationality','is_staff']

admin.site.register(User)
