from __future__ import unicode_literals

from django.db import models
from serviceprovider.models import Serviceprovider
from institution.models import Institution

# Create your models here.
class Availability(models.Model):
    
    status = models.IntegerField(choices=((0,"Available"),(1,"Unavailable")))
    daily = models.IntegerField(
        choices=(
        (0,"Monday"),
        (1,"Tuesday"),
        (2,"Wednesday"),
        (3,"Thursday"),
        (4,"Friday"),
        (5,"No daily availability")),
        default=5)
    weekly = models.BooleanField(default=False)
    starttime = models.TimeField()
    endtime = models.TimeField()
    serviceprovider = models.ForeignKey(Serviceprovider,on_delete=models.CASCADE,null=False,default=0)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)

    def __str__(self):
        return ";".join(["Name: " + str(self.serviceprovider),"Inst: " + str(self.institution),"Status: " + str(self.status)])
