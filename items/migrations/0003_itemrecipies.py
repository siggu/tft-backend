# Generated by Django 5.0.2 on 2024-03-16 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_effect'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRecipies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('element_item1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='element_item1', to='items.item')),
                ('element_item2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='element_item2', to='items.item')),
            ],
        ),
    ]