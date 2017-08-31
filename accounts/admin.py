# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj_1):
        return obj_1.description
    # изменяем отображение название столбца на свое
    user_info.short_description = 'Описание'

    def city(self, obj_2):
        return obj_2.city
    city.short_description      = 'Город'

    def phone(self, obj_3):
        return obj_3.phone
    phone.short_description     = 'Телефон'

    # сортировка объектов 
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
