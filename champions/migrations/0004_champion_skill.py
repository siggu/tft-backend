# Generated by Django 5.0.2 on 2024-03-05 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='champions.skill'),
        ),
    ]
