from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import *
class coreAdmin(BaseUserAdmin):
    ordering= ['id']
    list_display = ['name','mediator', 'lawyer_applicant', 'lawyer_defendant','client_applicant','client_defendant']

admin.site.register(Case)

admin.site.register(State)

admin.site.register(MediationPortafolio)

admin.site.register(MediationSessions)