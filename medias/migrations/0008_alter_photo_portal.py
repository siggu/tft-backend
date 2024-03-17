# Generated by Django 5.0.2 on 2024-03-16 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0007_merge_0006_photo_encounter_0006_photo_item'),
        ('portals', '0005_portaltype_alter_portal_portal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='portal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='portals.portaltype'),
        ),
    ]