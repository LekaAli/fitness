from __future__ import unicode_literals
from django.db import models


class ServiceProviderType(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'serviceprovider type'
        verbose_name_plural = 'serviceprovider types'

    def __unicode__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'speciality'
        verbose_name_plural = 'specialities'

    def __unicode__(self):
        return self.name


class Qualification(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'qualification'
        verbose_name_plural = 'qualifications'

    def __unicode__(self):
        return self.name


class ServiceProvider(models.Model):
    PERSON_STATUS = (
        (0, 'INACTIVE'),
        (1, 'ACTIVE'),
        (2, 'DELETED'),
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    sp_type = models.ForeignKey(ServiceProviderType, related_name='service_provider', blank=True, null=True,
                                on_delete=models.CASCADE)
    qualification = models.ManyToManyField(Qualification, related_name='service_providers', blank=True)
    speciality = models.ManyToManyField(Speciality, related_name='service_providers', blank=True)
    status = models.IntegerField(choices=PERSON_STATUS, default='0')
    email = models.EmailField()
    contact_number = models.IntegerField(max_length=10)
    alternate_number = models.IntegerField(max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'service provider'
        verbose_name_plural = 'service providers'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
