from django.db import models

# Create your models here.
dept=[
    ('Select Department','Select Department'),
    ('General Health','General Health'),
    ('Cardiology','Cardiology'),
    ('Dental','Dental'),
    ('Medical Research','Medical Research'),
]
class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    dob=models.DateField()
    department=models.CharField(max_length=100,choices=dept)
    mobileno=models.CharField(max_length=15)
    msg=models.TextField()
    apt_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
