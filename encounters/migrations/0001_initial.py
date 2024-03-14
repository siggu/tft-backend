# Generated by Django 5.0.2 on 2024-03-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description_1', models.TextField(blank=True, max_length=200)),
                ('description_2', models.TextField(blank=True, max_length=200)),
                ('description_3', models.TextField(blank=True, max_length=200)),
                ('description_4', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]