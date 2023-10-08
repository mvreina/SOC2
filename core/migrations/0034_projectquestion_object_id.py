# Generated by Django 4.2.4 on 2023-10-02 03:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_projectquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectquestion',
            name='object_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]