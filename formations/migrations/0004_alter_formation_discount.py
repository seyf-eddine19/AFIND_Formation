# Generated by Django 4.1.13 on 2024-05-19 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0003_enrollment_doctor_specialty_formation_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='discount',
            field=models.IntegerField(default=0, help_text='Enter a discount percentage between 0 and 100', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
