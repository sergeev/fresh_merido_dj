# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 100, default = '')
    website = models.URLField(default = '')
    phone = models.IntegerField(default = '')

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)

def save_create_profile(sender, instacne, **kwargs):
    instance.profile.save()
