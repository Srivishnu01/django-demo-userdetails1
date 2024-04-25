from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm, ProfileUpdateForm, PasswordChangeForm
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
            userid = f"{email_prefix}{phone_suffix}{user.registration_date.strftime('%d%m%Y')}"
            user.userid = userid
            user.save()
            # login(request, user)
            messages.success(request, 'Your account has been created successfully!')

            return redirect('profile', pk=user.pk)
    else:
        form = UserRegistrationForm()
    return render(request, 'reg_page.html', {'form': form})


def profile(request, pk):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)  # ,instance=request.user.profile)
        if form.is_valid():
            existing_profile = Profile.objects.filter(user_id=pk)
            if existing_profile:
                existing_profile.delete()
            print(pk)
            profile = form.save(commit=False)
            profile.user_id = pk
            profile.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile', pk=pk)
    else:
        # profile = Profile.objects.filter(user_id=pk)
        # if profile:
        #     form = ProfileUpdateForm(request.GET, instance=profile)
        # else:
        form = ProfileUpdateForm()
    pswd_field = request.build_absolute_uri().replace("profile", "change-password")
    # a_tag = f"""<a href="{pswd_field}">change my password</a>"""
    return render(request, 'profile.html',
                  {'form': form, 'pswd_field': pswd_field})


def home(request):
    return HttpResponse("Hello world!")


def password_changer(request, pk):
    print("hiiiiii98")
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            new_password = form.save(commit=False).newpassword
            CustomUser.objects.filter(pk=pk).update(mypassword=new_password)
    else:
        form = PasswordChangeForm()
    return render(request, 'pswd_changer.html', {'form': form})
