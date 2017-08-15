# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout

# Create your views here.
def home(request):
    #return HttpResponse("Welcome this is you first Django view page! :)")
    # accounts/templates/accounts/login.html
    numbers = [1,2,3,4,5]
    name = 'MayssAkaVasia'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html')

    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')


def logout(request):
    logout(request)

    return logout(request, 'accounts/login.html')

# Логика регистрации на сайте /account/
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return render(request, '/account/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})
