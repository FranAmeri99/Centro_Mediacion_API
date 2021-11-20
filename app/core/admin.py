from django.contrib import admin
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from core.models import *
class caseAdmin(admin.ModelAdmin):
 
    list_display = ('name','mediator', 'lawyer_applicant', 'lawyer_defendant','client_applicant','client_defendant')

class stateAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id','description')

class portfolioAdmin(admin.ModelAdmin):

    list_display = ('start_date','end_date', 'state', 'case')  

class sessionAdmin(admin.ModelAdmin):
  
    list_display = ('portfolio','date')

admin.site.register(Case,caseAdmin)

admin.site.register(State,stateAdmin)

admin.site.register(MediationPortafolio,portfolioAdmin)

admin.site.register(MediationSessions,sessionAdmin)
