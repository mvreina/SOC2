# Generated by Django 4.2.4 on 2023-10-07 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0101_alter_project_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='startDate',
            field=models.DateField(default=datetime.datetime(2023, 10, 7, 16, 46, 40, 492494), verbose_name='Fecha inicio'),
        ),
    ]