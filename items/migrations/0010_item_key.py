# Generated by Django 5.0.2 on 2024-03-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_item_ingamekey'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='key',
            field=models.CharField(default='Eng_Key', max_length=40),
        ),
    ]
