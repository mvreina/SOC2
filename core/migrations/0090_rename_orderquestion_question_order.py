# Generated by Django 4.2.4 on 2023-10-06 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_projectquestion_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='orderQuestion',
            new_name='order',
        ),
    ]
