# Generated by Django 5.0.2 on 2024-03-16 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0004_remove_portal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portal_type', models.CharField(choices=[('champ', 'Champ'), ('combat', 'Combat'), ('spatula', 'Spatula'), ('coin', 'Coin'), ('card', 'Card'), ('item', 'Item')], default='champ', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='portal',
            name='portal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portals.portaltype'),
        ),
    ]
