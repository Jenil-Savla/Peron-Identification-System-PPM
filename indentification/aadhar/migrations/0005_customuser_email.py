# Generated by Django 4.0.4 on 2022-05-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aadhar', '0004_remove_emailaddress_person_emailaddress_content_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]