# Generated by Django 3.1.1 on 2020-09-03 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20200903_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailentry',
            name='status',
        ),
        migrations.RemoveField(
            model_name='emailentry',
            name='updated',
        ),
    ]