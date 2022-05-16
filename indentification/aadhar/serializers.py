from rest_framework import serializers
from .models import CustomUser, Aadhar, Address, Qualification, Bank, PersonalDetails, EmailAddress, PhoneNumber, Experience

#import re

#email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class RegisterSerializer(serializers.ModelSerializer):
	password=serializers.CharField(max_length=32,min_length=8,write_only = True)
	class Meta:
		model = CustomUser
		fields = ['username','password','first_name','last_name']
		
	def validate(self,attrs):
		username = attrs.get('username',' ')

		if len(username)<5:
			raise serializers.ValidationError('Please enter a valid username')
		return attrs
		
	def create(self,validated_data):
            return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=32,min_length=8,write_only = True)
    class Meta:
        model = CustomUser
        fields = ['username','password']


class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = ['aadhar']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class EmailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = ['email']

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['phone',]


class PersonalDetailsSerializer(serializers.ModelSerializer):
    mails = EmailAddressSerializer(many = True)
    contacts = PhoneNumberSerializer(many = True)

    class Meta:
        model = PersonalDetails
        fields = '__all__'

    def create(self, validated_data):
        numbers = validated_data.pop("contacts")
        mails = validated_data.pop("mails")
        instance = super(PersonalDetailsSerializer, self).create(validated_data)
        for mail in mails:
            email = EmailAddress(**mail)
            email.content_object = instance
            email.save()
        for number in numbers:
            contact = PhoneNumber(**number)
            contact.content_object = instance
            contact.save()
        return instance

    def update(self, instance, validated_data):
        numbers = validated_data.pop("contacts")
        mails = validated_data.pop("mails")
        instance = super(PersonalDetailsSerializer, self).update(instance, validated_data)
        for number in numbers:
            contact = PhoneNumber(**number)
            contact.content_object = instance
            contact.save()
        for mail in mails:
            email = EmailAddress(**mail)
            email.content_object = instance
            email.save()
        return instance


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'