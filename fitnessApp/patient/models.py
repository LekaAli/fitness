from __future__ import unicode_literals

from django.db import models

# Create your models here.
class patient(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    fitness_club_name = models.TextField()
    trainer_id = models.TextField()
    