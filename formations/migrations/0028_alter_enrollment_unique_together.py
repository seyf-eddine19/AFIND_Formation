# Generated by Django 4.1.13 on 2024-06-27 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0027_delete_customgroup'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('formation', 'phone')},
        ),
    ]
