# Generated by Django 4.0.10 on 2024-09-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0022_rename_description_set12item_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set11item',
            old_name='description',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='set11item',
            name='tag1',
        ),
        migrations.RemoveField(
            model_name='set11item',
            name='tag2',
        ),
        migrations.RemoveField(
            model_name='set11item',
            name='tag3',
        ),
        migrations.AddField(
            model_name='set11item',
            name='affectedTraitKey',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='set11item',
            name='fromDesc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='set11item',
            name='ingameIcon',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='set11item',
            name='isHidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='set11item',
            name='imageUrl',
            field=models.URLField(),
        ),
    ]