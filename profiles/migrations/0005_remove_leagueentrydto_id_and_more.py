# Generated by Django 5.0.2 on 2024-05-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_leagueentrydto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leagueentrydto',
            name='id',
        ),
        migrations.AlterField(
            model_name='leagueentrydto',
            name='summonerId',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
    ]