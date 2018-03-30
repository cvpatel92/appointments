# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from scipy.signal._max_len_seq import max_len_seq

# Create your models here.
class AppointmentDetails(models.Model):
    date = models.CharField(max_length=50, default="")
    time = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=100, default="")
    
    class Meta:
        db_table = "AppointmentDetails"