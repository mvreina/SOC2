# Generated by Django 4.2.4 on 2023-09-30 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_projectquestion_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('checkbox', 'Checkbox'), ('radiobutton', 'Radio Button')], default='checkbox', max_length=12),
        ),
    ]
