from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from patient.models import Patient
from institution.models import Institution
from serviceProvider.models import Serviceprovider

# Create your models here.
class Referal(models.Model):
    id = models.AutoField(primary_key=True)
    referaldate = models.DateField(null=False,default=datetime.now())
    patient = models.ForeignKey(Patient,related_name='patient',on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution,related_name='institution',on_delete=models.CASCADE)
    serviceprovider = models.ForeignKey(Serviceprovider,related_name='serviceprovider',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patient','institution','serviceprovider','referaldate')
        ordering = ['id']

    def __unicode__(self):
        return 'Patient:%s - Institution:%s - Service Provider: %s ' % (self.patient,self.institution,self.serviceprovider)
    
    # def __str__(self):
    #     return ";".join(["Referal Date: " + str(self.referaldate),"Patient: " + str(self.patient), "Inst: " + str(self.institution), "service Provider: " + str(self.serviceprovider)])