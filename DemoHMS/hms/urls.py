import imp
from django.urls import path
from .views import *
#BASEURL = #http://127.0.0.1:8000/hms/

urlpatterns = [
    path('home/',view_home,name='home'),
    path('about/',view_about,name='about'),
    path('doctor/',view_doctor,name='doctor'),
    path('news/',view_news,name='news'),
    path('appointment/',view_appointment,name='appointment'),
]


