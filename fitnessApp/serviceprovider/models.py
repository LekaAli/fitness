from __future__ import unicode_literals
from django.db import models


class ServiceProviderType(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'Serviceprovider Type'
        verbose_name_plural = 'Serviceprovider Types'

    def __unicode__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

    def __unicode__(self):
        return self.name


class Qualification(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

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
    service_provider_type = models.ForeignKey(ServiceProviderType, related_name='service_provider', blank=True,
                                              null=True, on_delete=models.CASCADE)
    qualification = models.ManyToManyField(Qualification, related_name='service_providers', blank=True)
    speciality = models.ManyToManyField(Speciality, related_name='service_providers', blank=True)
    status = models.IntegerField(choices=PERSON_STATUS, default='0')
    email = models.EmailField(blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    alternate_number = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Service Provider'
        verbose_name_plural = 'Service Providers'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Availability(models.Model):
    DAYS = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    day_name = models.SmallIntegerField(choices=DAYS, blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    service_provider = models.ForeignKey('serviceprovider.ServiceProvider', related_name='daily_availability',
                                         blank=True, null=True, on_delete=models.CASCADE)
    institution = models.ForeignKey('institution.Institution', related_name='daily_availability', blank=True,
                                    null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Daily Availability'
        verbose_name_plural = 'Daily Availabilities'

    def __unicode__(self):
        return '%s: %s - %s' % (self.day_name, self.start_time, self.end_time)
