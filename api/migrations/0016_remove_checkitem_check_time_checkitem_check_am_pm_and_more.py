# Generated by Django 4.0 on 2022-02-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0015_alter_checkitem_options_alter_checkproject_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkitem',
            name='check_time',
        ),
        migrations.AddField(
            model_name='checkitem',
            name='check_am_pm',
            field=models.CharField(default='am', max_length=20),
        ),
        migrations.AddField(
            model_name='checkitem',
            name='check_date',
            field=models.DateTimeField(null=True, verbose_name='检查日期'),
        ),
    ]
