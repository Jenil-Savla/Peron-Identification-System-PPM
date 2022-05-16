from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class UserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        
        if not username:
            raise ValueError('Username is necessary')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


#Custom USer Model to handle multiple emails
class CustomUser(AbstractUser):
    email = None
    is_manager = models.BooleanField(default = False)

    REQUIRED_FIELDS=['first_name','last_name']
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        token = Token.objects.get(user=CustomUser.objects.get(self.id))
        return token


#AAdhar Table
class Aadhar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    aadhar = models.BigIntegerField(primary_key=True)
    active_aadhar = models.BooleanField(default = False)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.aadhar


#Address Table
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField(default = 000000)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user + "-" + self.postal_code


#Qualifications Table
class Qualification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    institute = models.CharField(max_length=100)
    year_of_passing = models.IntegerField()
    percentage = models.FloatField(default = 0.0)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user + "-" + self.institute


#Bank Details Table
class Bank(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user + "-" + self.bank_name



#One to Many relationship between Personal detials and email
class EmailAddress(models.Model):
    email = models.EmailField(("Email Address"),primary_key=True)

    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type","object_id")

    def __str__(self):
        return self.email


#One to Many relationship between Personal detials and phone number
class PhoneNumber(models.Model):
    phone = models.BigIntegerField(primary_key=True)

    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type","object_id")

    def __str__(self):
        return str(self.phone)


#Personal details Table
class PersonalDetails(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank =True, null =True)
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    contacts = GenericRelation(PhoneNumber)
    mails = GenericRelation(EmailAddress)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.blood_group


#Past Experience
class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=25)
    years_of_work = models.IntegerField()

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user + "-" + self.company_name