# Generated by Django 2.1.8 on 2020-04-04 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intworldapp', '0005_auto_20200330_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_img',
            field=models.ImageField(blank=True, null=True, upload_to='post/%Y/%m/%d'),
        ),
    ]