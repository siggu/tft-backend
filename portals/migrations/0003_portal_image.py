# Generated by Django 5.0.2 on 2024-03-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0002_portal_portal_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]