# Generated by Django 4.2.4 on 2023-10-29 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_projectpolicy_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpolicy',
            old_name='type',
            new_name='status',
        ),
    ]