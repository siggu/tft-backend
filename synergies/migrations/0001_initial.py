# Generated by Django 5.0.2 on 2024-03-05 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('champions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descriptoin', models.CharField(max_length=300)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='champions.champion')),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descriptoin', models.CharField(max_length=300)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origins', to='champions.champion')),
            ],
        ),
    ]
