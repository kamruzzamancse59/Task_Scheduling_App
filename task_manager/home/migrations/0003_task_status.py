# Generated by Django 4.2.4 on 2023-09-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_task_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Progress', 'Progress')], default='Pending', max_length=200),
        ),
    ]
