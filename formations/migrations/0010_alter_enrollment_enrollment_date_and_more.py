# Generated by Django 4.1.13 on 2024-05-20 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0009_alter_enrollment_enrollment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 19, 46, 12, 368557, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='enrollment_deadline',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 19, 46, 12, 360528, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
