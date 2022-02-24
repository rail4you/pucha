# Generated by Django 4.0 on 2022-02-18 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0011_timesheet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timesheet',
            options={'verbose_name': '时间表', 'verbose_name_plural': '时间表'},
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='check_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.checkproject'),
        ),
    ]
