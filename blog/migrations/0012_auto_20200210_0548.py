# Generated by Django 2.2 on 2020-02-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_regional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regional',
            name='user',
        ),
        migrations.AddField(
            model_name='regional',
            name='name',
            field=models.CharField(default=0, max_length=35),
        ),
    ]
