# Generated by Django 3.2.9 on 2021-11-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0006_photogallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='document',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]
