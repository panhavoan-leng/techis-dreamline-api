# Generated by Django 3.2.4 on 2021-09-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_images', '0002_backgroundimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundimage',
            name='image',
            field=models.ImageField(upload_to='uploads/images/', verbose_name='image'),
        ),
    ]
