# Generated by Django 4.2.4 on 2023-10-02 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_projectquestion_project_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectQuestion',
        ),
    ]
