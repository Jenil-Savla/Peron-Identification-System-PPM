# Generated by Django 4.0.4 on 2022-05-17 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aadhar', '0005_customuser_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='address',
            order_with_respect_to='user',
        ),
    ]
