from django.db import models


class mymodel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class CustomUser(mymodel):
    userid = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)
    mypassword = models.CharField(max_length=50)


class Profile(mymodel):
    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE,
                                to_field="userid")  # (CustomUser, on_delete=models.CASCADE, to_field="user_id")
    first_name = models.CharField(max_length=100, default="")
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, default="")
    father_name = models.CharField(max_length=100, default="")
    mother_name = models.CharField(max_length=100, default="")
    dob = models.DateField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class PasswordChange(mymodel):
    newpassword = models.CharField(max_length=50)
