# Generated by Django 5.0.2 on 2024-03-06 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0003_portal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portal',
            name='image',
        ),
    ]
