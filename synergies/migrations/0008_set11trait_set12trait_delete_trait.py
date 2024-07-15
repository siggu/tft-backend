# Generated by Django 5.0.2 on 2024-07-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synergies', '0007_alter_trait_ingamekey_alter_trait_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set11Trait',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ingameKey', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(blank=True, max_length=300)),
                ('imageUrl', models.URLField(default='https://cdn.lolchess.gg/upload/images/traits/Arcanist_normal_1709371622-arcanist.svg')),
                ('blackImageUrl', models.URLField(default='https://cdn.lolchess.gg/upload/images/traits/Arcanist_black_1709371622-arcanist.svg')),
                ('whiteImageUrl', models.URLField(default='https://cdn.lolchess.gg/upload/images/traits/Arcanist_white_1709371623-arcanist.svg')),
                ('_type', models.CharField(max_length=6)),
                ('style1', models.CharField(max_length=10)),
                ('style1_min', models.PositiveIntegerField(default=1)),
                ('style1_max', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style2', models.CharField(blank=True, max_length=10, null=True)),
                ('style2_min', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style2_max', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style3', models.CharField(blank=True, max_length=10, null=True)),
                ('style3_min', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style3_max', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style4', models.CharField(blank=True, max_length=10, null=True)),
                ('style4_min', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('stats1', models.TextField(blank=True, max_length=200, null=True)),
                ('stats2', models.TextField(blank=True, max_length=100, null=True)),
                ('stats3', models.TextField(blank=True, max_length=100, null=True)),
                ('stats4', models.TextField(blank=True, max_length=100, null=True)),
                ('stats5', models.TextField(blank=True, max_length=100, null=True)),
                ('stats6', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Set12Trait',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ingameKey', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(blank=True, max_length=300)),
                ('imageUrl', models.URLField(default='https://cdn.lolchess.gg/upload/images/traits/Arcanist_normal_1709371622-arcanist.svg')),
                ('blackImageUrl', models.URLField(default='https://cdn.lolchess.gg/upload/images/traits/Arcanist_black_1709371622-arcanist.svg')),
                ('whiteImageUrl', models.URLField(default='https://cdn.lolchess.gg/upload/images/traits/Arcanist_white_1709371623-arcanist.svg')),
                ('_type', models.CharField(max_length=6)),
                ('style1', models.CharField(max_length=10)),
                ('style1_min', models.PositiveIntegerField(default=1)),
                ('style1_max', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style2', models.CharField(blank=True, max_length=10, null=True)),
                ('style2_min', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style2_max', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style3', models.CharField(blank=True, max_length=10, null=True)),
                ('style3_min', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style3_max', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('style4', models.CharField(blank=True, max_length=10, null=True)),
                ('style4_min', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('stats1', models.TextField(blank=True, max_length=200, null=True)),
                ('stats2', models.TextField(blank=True, max_length=100, null=True)),
                ('stats3', models.TextField(blank=True, max_length=100, null=True)),
                ('stats4', models.TextField(blank=True, max_length=100, null=True)),
                ('stats5', models.TextField(blank=True, max_length=100, null=True)),
                ('stats6', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Trait',
        ),
    ]
