# Generated by Django 2.1.8 on 2020-03-22 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intworlduser', '0003_auto_20200322_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
