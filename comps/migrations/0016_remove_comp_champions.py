# Generated by Django 5.0.2 on 2024-04-02 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0015_remove_compelement_ele_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comp',
            name='champions',
        ),
    ]
