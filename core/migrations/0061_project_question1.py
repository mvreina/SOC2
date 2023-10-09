# Generated by Django 4.2.4 on 2023-10-02 16:34

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_projectquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='question1',
            field=multiselectfield.db.fields.MultiSelectField(choices=[{'Respuesta 1', '1'}, {'Respuesta 2', '2'}, {'3', 'Respuesta 3'}, {'Respuesta 4', '4'}, {'Respuesta 5', '5'}], default='', max_length=11),
        ),
    ]
