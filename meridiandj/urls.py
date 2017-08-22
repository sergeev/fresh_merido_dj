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
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # glogal website page /meridiancore/*
    url(r'^$', views.home_page_global, name = 'home_page_global'),
    #url(r'^$', views.login_redirect, name = 'login_redirect'),
    url(r'^account/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
]
