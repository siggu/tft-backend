# Generated by Django 5.0.2 on 2024-03-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synergies', '0012_job_champion_origin_champion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='champion',
        ),
        migrations.RemoveField(
            model_name='origin',
            name='champion',
        ),
    ]