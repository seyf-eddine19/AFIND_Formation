# Generated by Django 4.1.13 on 2024-06-04 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0022_sitesettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='email_backend',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='email_host',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='email_host_password',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='email_host_user',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='email_port',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='email_use_tls',
        ),
    ]
