# Generated by Django 4.2.4 on 2023-10-06 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_remove_projectquestion_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectquestion',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.project', verbose_name='Proyecto'),
        ),
    ]
