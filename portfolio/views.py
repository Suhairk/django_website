import os
import mimetypes
import re
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import projects,form

# Create your views here.

project = projects.objects.all()

def home(request):
    if request.method=='POST':

        #print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']        

        #print(name, email, phone ,message)
        ins=form(name=name , email= email , phone=phone ,message=message)
        
        ins.save()
        #print("data saved")
    return render(request , 'index.html',{'project':project})

def details(request):
    return render(request ,'portfolio-details.html',{'project':project})

def download(request):
    # fill these variables with real values
    fl_path = 'media/ExpResume.pdf'
    filename = 'download.pdf'
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response