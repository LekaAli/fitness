from __future__ import unicode_literals

from django.db import models

# Create your models here.
class doctor(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    qualification = models.TextField()
    institution_name = models.TextField()