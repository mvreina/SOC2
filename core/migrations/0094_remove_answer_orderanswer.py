# Generated by Django 4.2.4 on 2023-10-06 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_remove_question_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='orderAnswer',
        ),
    ]
