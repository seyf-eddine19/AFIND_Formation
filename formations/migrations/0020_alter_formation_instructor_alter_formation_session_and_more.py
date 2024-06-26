# Generated by Django 4.1.13 on 2024-06-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0019_formation_session_alter_formation_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='instructor',
            field=models.CharField(blank=True, default=0, max_length=560),
        ),
        migrations.AlterField(
            model_name='formation',
            name='session',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='formation',
            unique_together={('title', 'session')},
        ),
    ]
