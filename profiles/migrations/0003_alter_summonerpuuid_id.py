# Generated by Django 4.0.10 on 2024-08-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_leagueentrydto_remove_summonerpuuid_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summonerpuuid',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]