# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfileManager(models.Manager):
    def get_queryset(self):
        # фильтер
        return super(UserProfileManager, self).get_queryset().filter(city = 'Moskow')
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 100, default = '')
    website = models.URLField(default = '')
    phone = models.IntegerField(default = '')
    # создаем папку(profile_image) и загружаем туда изображения
    image = models.ImageField(upload_to = 'profile_image', blank = True)

    # пример обращения к фильтру
    Moskow = UserProfileManager()

    """
    Вывод пользователя, если не применять, пользователь будет скрыт!
    UserProfile Object
    """
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)

def save_create_profile(sender, instacne, **kwargs):
    instance.profile.save()
