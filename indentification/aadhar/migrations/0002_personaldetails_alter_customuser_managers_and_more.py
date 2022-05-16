# Generated by Django 4.0.4 on 2022-05-16 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aadhar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100)),
                ('year_of_passing', models.IntegerField()),
                ('percentage', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aadhar.personaldetails')),
            ],
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_role', models.CharField(max_length=25)),
                ('years_of_work', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Email Address')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aadhar.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('aadhar', models.BigIntegerField(primary_key=True, serialize=False)),
                ('active_aadhar', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
