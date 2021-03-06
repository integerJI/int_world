# Generated by Django 2.1.8 on 2020-03-30 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intworldapp', '0004_auto_20200330_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date published'),
        ),
    ]
