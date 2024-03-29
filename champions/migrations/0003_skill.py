# Generated by Django 5.0.2 on 2024-03-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('skill_type', models.CharField(choices=[('active', 'Active'), ('passive', 'Passive')], max_length=10)),
                ('description', models.CharField(max_length=300)),
                ('avatar', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
