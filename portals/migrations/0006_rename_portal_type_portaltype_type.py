# Generated by Django 5.0.2 on 2024-03-16 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0005_portaltype_alter_portal_portal_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portaltype',
            old_name='portal_type',
            new_name='type',
        ),
    ]