# Generated by Django 3.0.5 on 2020-04-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barber',
            old_name='yearsOfExperience',
            new_name='experience',
        ),
    ]
