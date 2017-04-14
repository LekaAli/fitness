from __future__ import unicode_literals

from django.db import models

# Create your models here.
class specialist(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    qualification = models.TextField()
    speciality = models.TextField()
    institution_name = models.TextField()

class availability(models.Model):
    
    availability_status = models.TextField() # when is the doc/specilist available (e.g. day, night and weekend) type(e.g. Emergency and general consultation(e.g. advise))
    institution_name = models.TextField()
    availability_time_frame = models.TextField()


class payment_option(models.Model):
    payment_type = models.TextField() # deposit, eft, on consultation and etc
    amount = models.TextField() # type of service 
