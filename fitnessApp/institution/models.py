from __future__ import unicode_literals
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=300, default='', unique=True)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __unicode__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    region = models.ManyToManyField(Region, related_name='regions', blank=True)

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=128, default='')
    region = models.ForeignKey(Region, related_name='location', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, default='', unique=True)
    description = models.CharField(max_length=300, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Institution(models.Model):
    STATUS = (
        (0, 'INACTIVE'),
        (1, 'ACTIVE'),
        (2, 'DELETED'),
    )
    name = models.CharField(max_length=300, default='', db_index=True)
    province = models.ForeignKey(Province, related_name='institution', blank=True, null=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, related_name='institution', blank=True, null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='institution', blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='institution', blank=True, null=True, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    def __unicode__(self):
        return self.name

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, name):
        self.name = name

    def get_service_provider(self):
        pass

    def deactivate_service_provider(self):
        pass



