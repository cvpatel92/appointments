# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from models import AppointmentDetails
import json


# Create your views here.
def crudops(request):
    if request.method == "POST":
        if request.POST.get('date') != None:  
            ad = AppointmentDetails(
                date=request.POST.get('date'),
                time=request.POST.get('time'),
                desc=request.POST.get('desc')
                )
            ad.save()        
        elif request.POST.has_key('client_response'):
            x = request.POST['client_response']                         
            objects = json.dumps([dict(item) for item in AppointmentDetails.objects.filter(desc__icontains=x).values('date', 'time', 'desc')])                                                                                         
            return HttpResponse(objects, content_type='application/javascript') 
        else:
            return render_to_response('apnmt.html', context_instance=RequestContext(request))
         
        return render(request, "apnmt.html", locals())
    
    else:
        return render(request, "apnmt.html", locals())
