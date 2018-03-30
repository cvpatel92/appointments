from django.conf.urls import url
from django.contrib import admin
import atservices.views

urlpatterns = [
    url(r'^general/$', atservices.views.crudops, name="AppointmentDetails")
]