# Generated by Django 2.1.8 on 2020-04-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intworldapp', '0012_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='intworldapp.Tag'),
        ),
    ]
