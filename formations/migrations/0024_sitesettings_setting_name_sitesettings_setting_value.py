# Generated by Django 4.1.13 on 2024-06-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0023_remove_sitesettings_email_backend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='setting_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='setting_value',
            field=models.TextField(blank=True),
        ),
    ]