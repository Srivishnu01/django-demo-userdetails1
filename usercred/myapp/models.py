from django.db import models


class CustomUser(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, to_field="user_id")
    first_name = models.CharField(max_length=100, default="")
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, default="")
    father_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    dob = models.DateField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
