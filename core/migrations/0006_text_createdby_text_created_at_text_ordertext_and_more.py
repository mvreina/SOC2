# Generated by Django 4.2.4 on 2023-10-28 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_answer_excludedpolicies'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='createdBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='textCreatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AddField(
            model_name='text',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text',
            name='orderText',
            field=models.PositiveIntegerField(default=1, verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='text',
            name='updatedBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='textUpdatedBy', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado por'),
        ),
        migrations.AddField(
            model_name='text',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]