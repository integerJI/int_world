# Generated by Django 2.1.8 on 2020-04-15 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intworldapp', '0009_auto_20200415_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag_set',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
