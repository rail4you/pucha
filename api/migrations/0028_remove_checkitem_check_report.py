# Generated by Django 4.0 on 2022-02-19 07:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0027_checkproject_left_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkitem',
            name='check_report',
        ),
    ]
