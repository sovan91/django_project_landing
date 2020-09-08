# Generated by Django 3.1.1 on 2020-09-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(default='', max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]