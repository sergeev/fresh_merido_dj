# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import views as logout
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.urls import reverse
"""
Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
"""


def home(request):
    # accounts/templates/accounts/login.html
    numbers = [1,2,3,4,5]
    name = 'MayssAkaVasia'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html')

    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

# Логика регистрации на сайте /account/
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
        return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

#@login_required
def view_profile(request):
    args = {'user': request.user }
    return render(request, 'accounts/view_profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form': form }
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST or None, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form': form }
        return render(request, 'accounts/change_password.html', args)
