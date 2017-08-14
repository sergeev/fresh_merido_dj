# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    #return HttpResponse("Welcome this is you first Django view page! :)")
    # accounts/templates/accounts/login.html
    numbers = [1,2,3,4,5]
    name = 'MayssAkaVasia'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
