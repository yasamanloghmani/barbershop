# Generated by Django 3.0.5 on 2020-04-12 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200408_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('M', 'Morning'), ('N', 'Noon'), ('E', 'Evening')], default='M', max_length=1)),
                ('skill', models.CharField(choices=[('H', 'Hair-Cut'), ('C', 'Hair-Color'), ('N', 'Nail')], default='H', max_length=1)),
                ('customer', models.CharField(max_length=50)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Barber')),
            ],
        ),
    ]
