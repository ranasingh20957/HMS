from django.shortcuts import render
from .forms import AppointmentForm
# Create your views here.


def view_home(request):
    resp=render(request,'hms/home.html')
    return resp

def view_about(request):
    resp=render(request,'hms/about.html')
    return resp    

def view_doctor(request):
    resp=render(request,'hms/doctor.html')
    return resp  

def view_news(request):
    resp=render(request,'hms/news.html')
    return resp 

def view_appointment(request):
    if request.method=='GET':
        frm_unbound=AppointmentForm()
        d1={'form':frm_unbound}
        resp=render(request,'hms/appointment.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=AppointmentForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            d1={'msg':'Patent Appointment Saved!!'}
            resp=render(request,'hms/appointment.html',context=d1)
            return resp
        else:
            d1={'form':frm_bound}
            resp=render(request,'hms/appointment.html',context=d1)
            return resp

      
