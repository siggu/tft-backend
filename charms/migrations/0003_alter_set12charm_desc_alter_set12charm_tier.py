# Generated by Django 4.0.10 on 2024-09-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charms', '0002_alter_set12charm_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set12charm',
            name='desc',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='set12charm',
            name='tier',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
