# Generated by Django 4.1.13 on 2024-05-27 19:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0013_alter_enrollment_enrollment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='enrollment_deadline',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
