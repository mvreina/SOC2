# Generated by Django 4.2.4 on 2023-10-02 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_projectquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectquestion',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='core.project', verbose_name='Proyecto'),
        ),
        migrations.AddField(
            model_name='projectquestion',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='core.question', verbose_name='Pregunta'),
        ),
    ]
