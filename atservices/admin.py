# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from atservices.models import AppointmentDetails


# Register your models here.
class AppointmentDetailsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'desc')
    
admin.site.register(AppointmentDetails, AppointmentDetailsAdmin)