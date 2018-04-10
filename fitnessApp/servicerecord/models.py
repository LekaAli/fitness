# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class ServiceRecord(models.Model):
    service_name = models.CharField(max_length=128, blank=True, null=True)
    service_description = models.CharField(max_length=500, blank=True, null=True)
    patient = models.ForeignKey('patient.Patient', related_name='service_record', blank=True, null=True,
                                on_delete=models.CASCADE)
    institution = models.ForeignKey('institution.Institution', related_name='service_record', blank=True, null=True,
                                    on_delete=models.CASCADE)
    service_provider = models.ForeignKey('serviceprovider.ServiceProvider', related_name='service_record', blank=True,
                                         null=True, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Service Record'
        verbose_name_plural = 'Service Records'

    def __unicode__(self):
        return self.service_name
