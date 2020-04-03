# Generated by Django 2.2 on 2020-02-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_delete_clinicalmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinicalmanager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofdepartment', models.CharField(max_length=30)),
                ('partgrp', models.CharField(max_length=30)),
                ('descrptn', models.CharField(max_length=30)),
                ('dte', models.CharField(max_length=30)),
                ('nameofclinicalengr', models.CharField(max_length=30)),
                ('nameofhospital', models.CharField(max_length=30)),
                ('ceid', models.CharField(max_length=30)),
                ('ponumber', models.CharField(max_length=30)),
                ('prnumber', models.CharField(max_length=30)),
                ('status', models.CharField(default='new', max_length=30)),
            ],
        ),
    ]
