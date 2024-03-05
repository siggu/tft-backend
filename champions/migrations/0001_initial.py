# Generated by Django 5.0.2 on 2024-03-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cost', models.PositiveIntegerField()),
                ('health', models.PositiveIntegerField(default=100)),
                ('ad', models.PositiveIntegerField(default=10)),
                ('dps', models.PositiveIntegerField(default=10)),
                ('attack_range', models.PositiveIntegerField(default=1)),
                ('attack_speed', models.DecimalField(decimal_places=2, default=1, max_digits=3)),
                ('armor', models.PositiveIntegerField(default=10)),
                ('magic_resistance', models.PositiveIntegerField(default=10)),
                ('avatar', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
