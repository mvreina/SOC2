# Generated by Django 4.2.4 on 2023-10-02 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_projectquestion_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectquestion',
            name='object_id',
        ),
    ]
