# Generated by Django 5.0.2 on 2024-03-06 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0006_remove_champion_dps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='avatar',
        ),
    ]