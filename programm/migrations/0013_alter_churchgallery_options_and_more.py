# Generated by Django 4.0.2 on 2023-04-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programm', '0012_pastors_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='churchgallery',
            options={'ordering': ['-eventDate'], 'verbose_name_plural': 'Church Gallery'},
        ),
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'ordering': ['-eventImg'], 'verbose_name_plural': 'Image Gallery'},
        ),
    ]