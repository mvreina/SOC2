# Generated by Django 4.2.4 on 2023-09-25 02:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_project_numquestion_project_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='project_question',
            new_name='ProjectQuestion',
        ),
        migrations.AlterModelOptions(
            name='projectquestion',
            options={'verbose_name': 'Proyecto - Preguntas', 'verbose_name_plural': 'Projectos - Preguntas'},
        ),
    ]
