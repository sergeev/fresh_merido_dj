# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 100, default = '')
    website = models.URLField(default = '')
    phone = models.IntegerField(default = '')

#@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user = instance)

# При исполнени выдает ошибку
#post_save.connect(create_profile, sender = User)
