# Generated by Django 2.2 on 2020-02-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_clinicalmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
