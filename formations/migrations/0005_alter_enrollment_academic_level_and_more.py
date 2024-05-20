# Generated by Django 4.1.13 on 2024-05-19 15:39

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0004_alter_formation_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='academic_level',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='department',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='doctor_specialty',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 19, 16, 39, 53, 327905), null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], default='Pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='formation',
            name='discount',
            field=models.IntegerField(default=0, help_text='Enter a discount percentage between 0 and 100', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='formation',
            name='enrollment_deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 19, 16, 39, 53, 327905), null=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='instructor',
            field=models.CharField(max_length=560, null=True),
        ),
    ]
