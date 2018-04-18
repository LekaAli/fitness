from __future__ import unicode_literals
from django.db import models
from serviceprovider.models import ServiceProvider
from institution.models import Institution


class Assignment(models.Model):
    STATUS_OPTIONS = (
        (0, 'ACTIVE'),
        (1, 'INACTIVE')
    )
    service_provider = models.ForeignKey(ServiceProvider, related_name='assignment', blank=True, null=True,
                                         on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, related_name='assignment', blank=True, null=True,
                                    on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_OPTIONS, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __unicode__(self):
        return '%s - %s - %s' % (self.service_provider, self.institution, self.status)
