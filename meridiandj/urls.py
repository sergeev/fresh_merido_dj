# -*- coding: utf-8 -*-
"""meridiandj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from meridiandj import views
from django.conf import settings
from django.conf.urls.static import static

"""
    accounts используеться в шаблоне accounts/templates/accounts/home.html
    <li><a href="{% url 'accounts:view_profile' %}">Профиль</a></li>
    <li><a href="{% url 'accounts:edit_profile' %}">Изменить профиль</a></li>
"""

urlpatterns = [
    # glogal website page /meridiancore/*
    url(r'^$', views.home_page_global, name = 'home_page_global'),
    #url(r'^$', views.login_redirect, name = 'login_redirect'),
    url(r'^account/', include('accounts.urls', namespace = 'accounts')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
