# Generated by Django 4.1.13 on 2024-05-19 20:21

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0005_alter_enrollment_academic_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='places_left',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 19, 21, 21, 9, 172581), null=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='enrollment_deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 19, 21, 21, 9, 172581), null=True),
        ),
    ]
