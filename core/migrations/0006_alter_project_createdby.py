# Generated by Django 4.2.4 on 2023-09-20 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_project_created_at_project_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdBy', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
    ]