# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from meridiancore import views

# Create your views here.
def home_page(request):
    return render(request, 'meridian/default.html')
