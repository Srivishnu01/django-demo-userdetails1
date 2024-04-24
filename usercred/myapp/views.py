from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import CustomUser, Profile
from datetime import datetime


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email_prefix = user.email[:3]
            phone_suffix = user.phone_number[-5:]
            user.registration_date = datetime.now()
            user_id = f"{email_prefix}{phone_suffix}{user.registration_date.strftime('%d%m%Y')}"
            user.user_id = user_id
            user.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'reg_page.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})


def home(request):
    return HttpResponse("Hello world!")
