# Generated by Django 5.0.2 on 2024-03-14 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encounters', '0001_initial'),
        ('medias', '0005_alter_photo_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='encounter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='encounters.encounter'),
        ),
    ]
