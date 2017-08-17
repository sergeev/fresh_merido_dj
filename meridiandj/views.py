# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.

def login_redirect(request):
    return redirect('account/login')

def home_page_global(request):
    return render(request, 'meridian/default.html')
