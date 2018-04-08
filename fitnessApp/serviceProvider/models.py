from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Serviceprovider(models.Model):

    DOCTOR = 'Doctor'
    TRAINER = 'Trainer'
    SPECIALIST = 'Specialist'
    TYPE = (
            (DOCTOR,'Doctor'),
            (TRAINER,'Trainer'),
            (SPECIALIST,'Specialist'),
        )   
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    category = models.CharField(max_length=25,choices=TYPE)
    qualification = models.CharField(max_length=25)
    speciality = models.CharField(max_length=25)
    status = models.IntegerField(choices=((0,'created'),(2,'updated'),(3,'deleted')),default='0')
    creationdate = models.DateField(null=False,default=timezone.now())

    # def __unicode__(self):
    #     return '%s %s : %s' % (self.firstname,self.lastname,self.category)

    # def __str__(self):
    #     return self.lastname