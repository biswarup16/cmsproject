# Generated by Django 3.2.9 on 2021-11-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photogallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photogallery', models.ImageField(upload_to='about')),
                ('phototitle', models.CharField(max_length=30)),
            ],
        ),
    ]
