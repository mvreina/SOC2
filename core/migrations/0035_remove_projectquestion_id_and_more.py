# Generated by Django 4.2.4 on 2023-10-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_projectquestion_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectquestion',
            name='id',
        ),
        migrations.AlterField(
            model_name='projectquestion',
            name='object_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]