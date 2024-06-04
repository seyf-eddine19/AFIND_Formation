# Generated by Django 4.1.13 on 2024-06-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0020_alter_formation_instructor_alter_formation_session_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='formation',
            name='session',
            field=models.CharField(max_length=200, null=True),
        ),
    ]