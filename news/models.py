# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Создаем модель для news
class News(models.Model):
    class Meta:
        # описываем название базы данных под себя
        db_table = "news"
    news_title = models.CharField(max_lenght = 200)
    news_content = models.TextField(max_lenght = 10000)
    news_alies = models.CharField(max_lenght = 200)
    news_date_created = models.DataTimeField()
    new_created_by_user =
    news_likes = models.Integer()
