# Generated by Django 4.1.5 on 2023-01-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='images',
            field=models.ImageField(default='5b7.jpg', upload_to='album_pictures'),
        ),
    ]
