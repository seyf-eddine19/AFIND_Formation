# Generated by Django 4.1.13 on 2024-06-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0028_alter_enrollment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='phone',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]