# Generated by Django 4.2.4 on 2023-10-02 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0053_alter_projectquestion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectquestion',
            options={'verbose_name': 'Proyecto - Preguntas', 'verbose_name_plural': 'Projectos - Preguntas'},
        ),
        migrations.RemoveField(
            model_name='projectquestion',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='projectquestion',
            name='userAnswer',
        ),
        migrations.AddField(
            model_name='projectquestion',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='core.question', verbose_name='Pregunta'),
        ),
        migrations.AlterField(
            model_name='projectquestion',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_question', to='core.project', verbose_name='Proyecto'),
        ),
        migrations.CreateModel(
            name='ProjectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAnswer', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('answer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='core.answer', verbose_name='Respuesta')),
                ('createdBy', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_answerCreatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_answer', to='core.project', verbose_name='Proyecto')),
                ('updatedBy', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_answerUpdatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por')),
            ],
            options={
                'verbose_name': 'Proyecto - Respuestas',
                'verbose_name_plural': 'Projectos - Respuestas',
            },
        ),
    ]
