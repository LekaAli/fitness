from __future__ import unicode_literals
from django.db import models
from rest_framework import serializers


class Relationship(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'relationship'
        verbose_name_plural = 'relationships'

    def __unicode__(self):
        return self.name


class NextOfKin(models.Model):
    first_name = models.CharField(max_length=128, default='')
    last_name = models.CharField(max_length=128, default='')
    contact_number = models.IntegerField()
    relationship = models.ForeignKey(Relationship, related_name='next_of_kin', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'next of kin'
        verbose_name_plural = 'next of kins'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Patient(models.Model):
    PATIENT_STATUS = (
        (0, 'INACTIVE'),
        (1, 'ACTIVE'),
        (2, 'DELETED'),
    )
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    identity_number = models.CharField(max_length=13, default='', unique=True)
    province = models.ForeignKey('institution.Province', related_name='patient', blank=True, null=True,
                                 on_delete=models.CASCADE)
    region = models.ForeignKey('institution.Region', related_name='patient', blank=True, null=True,
                              on_delete=models.CASCADE)
    location = models.ForeignKey('institution.Location', related_name='patient', blank=True, null=True,
                                 on_delete=models.CASCADE)
    next_of_kin = models.ForeignKey(NextOfKin, related_name='patient', blank=True, null=True, on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    status = models.IntegerField(choices=PATIENT_STATUS, default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patients'
        unique_together = ('first_name', 'last_name', 'identity_number', )

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def retrieve_service_record(self):
        pass

    def request_appointment(self):
        pass



