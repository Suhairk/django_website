import mimetypes
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
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


def download_res(request):
    # fill these variables with real values
    fl_path = '/home/imsuhair/django_website/media/Suhair_Ai-python.pdf'
    filename = 'Res_suhair_python_ai.pdf'
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_cover(request):
    # fill these variables with real values
    fl_path = '/home/imsuhair/django_website/media/Suhair_coverLetter.pdf'
    filename = 'Cov_suhair_Ai_python.pdf'
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
