from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class  Institution(models.Model):
    CATEGORY = (
            (0,"General Practitioner"),
            (1,"Hospital"),
            (2,"Fitness Centre"),
            (3,"Clinic"),
            (4,"School"),
            )
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    category = models.IntegerField(max_length=200,choices=CATEGORY)
    status = models.IntegerField(choices=((0,'created'),(1,'updated'),(2,'deleted')),default=0)
    creationdate = models.DateField(null=False,default=timezone.now())

    # def __unicode__(self):
    #     return self.name
    # def __str__(self):
    #     return "Institution: " + self.name
        
        
