# Generated by Django 4.2.4 on 2023-10-02 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0032_delete_projectquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None - None', max_length=200, verbose_name='Nombre del proyecto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('createdBy', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_questionCreatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='core.project', verbose_name='Proyecto')),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='core.question', verbose_name='Pregunta')),
                ('updatedBy', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_questionUpdatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'Proyecto - Preguntas',
                'verbose_name_plural': 'Projectos - Preguntas',
            },
        ),
    ]
