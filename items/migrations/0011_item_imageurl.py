# Generated by Django 5.0.2 on 2024-03-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_item_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imageUrl',
            field=models.URLField(default='https://ih1.redbubble.net/image.2477120866.6033/raf,750x1000,075,t,101010:01c5ca27c6.u1.jpg'),
        ),
    ]