# Generated by Django 4.2.4 on 2023-10-28 03:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_answer_excludedpolicies'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='excludedPolicies',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Política 1'), (2, 'Política 2'), (3, 'Política 3'), (4, 'Política 4'), (5, 'Política 5'), (6, 'Política 6'), (7, 'Política 7'), (8, 'Política 8'), (9, 'Política 9'), (10, 'Política 10'), (11, 'Política 11'), (12, 'Política 12'), (13, 'Política 13'), (14, 'Política 14'), (15, 'Política 15'), (16, 'Política 16'), (17, 'Política 17'), (18, 'Política 18'), (19, 'Política 19'), (20, 'Política 20'), (21, 'Política 21'), (22, 'Política 22'), (23, 'Política 23'), (24, 'Política 24'), (25, 'Política 25'), (26, 'Política 26'), (27, 'Política 27'), (28, 'Política 28'), (29, 'Política 29'), (30, 'Política 30'), (31, 'Política 31'), (32, 'Política 32')], default=[1], max_length=100, null=True, verbose_name='Políticas excluidas'),
        ),
    ]
