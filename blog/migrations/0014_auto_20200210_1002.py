# Generated by Django 2.2 on 2020-02-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourcingTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Requestforregionalmanager',
        ),
    ]
