from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Aadhar, Address, Qualification, Bank, PersonalDetails, EmailAddress, PhoneNumber, Experience

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Aadhar)
admin.site.register(Address)
admin.site.register(Qualification)
admin.site.register(Bank)
admin.site.register(PersonalDetails)
admin.site.register(EmailAddress)
admin.site.register(PhoneNumber)
admin.site.register(Experience)