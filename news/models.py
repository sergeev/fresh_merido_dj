# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Создаем модель для news
# class News(models.Model):
#     class Meta:
#         # описываем название базы данных под себя
#         db_table = "news"
#     title = models.CharField()
#     content = models.TextField()
#     alies = models.CharField()
#     date_created = models.DataTimeField()
#     created_by_user = models.OneToOneField(User)
#     likes = models.IntegerField()
