# Generated by Django 2.2 on 2020-02-03 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_areamanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areamanager',
            name='approval',
        ),
        migrations.RemoveField(
            model_name='areamanager',
            name='user',
        ),
    ]