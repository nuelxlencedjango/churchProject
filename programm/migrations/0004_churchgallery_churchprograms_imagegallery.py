# Generated by Django 4.0.2 on 2023-02-24 21:26

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programm', '0003_donationandoffering'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('eventDate', models.DateTimeField(blank=True, null=True)),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChurchPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('mesg', models.TextField(blank=True, max_length=500, null=True)),
                ('date_paid', models.DateTimeField(blank=True, null=True)),
                ('img', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('venue', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('eventImg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university_requiremeents', to='programm.churchgallery')),
            ],
            options={
                'verbose_name_plural': 'Image Gallery',
            },
        ),
    ]
