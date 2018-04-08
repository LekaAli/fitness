from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from serviceProvider.models import Serviceprovider
from institution.models import Institution
from rest_framework import serializers

class Assignment(models.Model):
    
    date = models.DateField(null=False,default=timezone.now())
    serviceprovider = models.ForeignKey(Serviceprovider,related_name='assignment',on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    status = models.IntegerField(choices=((0,'active'),(1,'inactive')),default=0)

    def __unicode__(self):
        return '%d: %s' % (self.id,str(self.institution.name))
