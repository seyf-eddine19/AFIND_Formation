# Generated by Django 4.1.13 on 2024-05-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0014_alter_enrollment_enrollment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='map_iframe',
            field=models.TextField(blank=True, help_text='iframe of the location on the map', max_length=800, null=True),
        ),
    ]
