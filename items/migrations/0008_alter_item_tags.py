# Generated by Django 5.0.2 on 2024-03-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_item_composition1_item_composition2_item_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.TextField(choices=[('basic', 'Basic'), ('normal', 'Normal'), ('emblem', 'Emblem'), ('support', 'Support'), ('artifact', 'Artifact'), ('radiant', 'Radiant')], default='Normal'),
        ),
    ]
