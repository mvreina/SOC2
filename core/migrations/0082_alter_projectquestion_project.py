# Generated by Django 4.2.4 on 2023-10-06 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_remove_projectquestion_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectquestion',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.project', verbose_name='Proyecto'),
        ),
    ]