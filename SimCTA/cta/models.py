from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Course(models.Model):

    name = models.CharField((_('Name')), max_length=100)
    description = models.TextField((_('Description')), blank=True)
    duration = models.DurationField(_('Duration in weeks')) 
    value = models.DecimalField((_('Value')), max_digits=6, decimal_places=2)
    status = models.BooleanField(_('Active?'), default=True)
    created_updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name