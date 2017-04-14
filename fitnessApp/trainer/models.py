from __future__ import unicode_literals

from django.db import models

# Create your models here.

class trainer(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    qualification = models.TextField()
    specialisation = models.TextField() # what you specilize in (e.g. Strength,conditioning, special population and need)
    fitness_center_name = models.TextField() # fitness center 
    location = models.TextField() #
    
