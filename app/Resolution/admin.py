from django.contrib import admin

from Resolution.models import *
class AdminResolution():
    ordering = ['id']
    list_display = ['description', 'date']


admin.site.register(Resolution)