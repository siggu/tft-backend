# Generated by Django 5.0.2 on 2024-07-15 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0002_set11champion_set12champion'),
        ('comps', '0005_set11comp_set11compelement_set11itemusage_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Champion',
        ),
    ]
