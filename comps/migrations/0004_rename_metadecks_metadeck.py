# Generated by Django 5.0.2 on 2024-07-11 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comps", "0003_itemusage_metadecks"),
    ]

    operations = [
        migrations.RenameModel(old_name="MetaDecks", new_name="MetaDeck",),
    ]
