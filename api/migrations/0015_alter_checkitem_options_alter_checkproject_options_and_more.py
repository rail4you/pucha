# Generated by Django 4.0 on 2022-02-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_checkitem_check_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkitem',
            options={'verbose_name': '检查项目', 'verbose_name_plural': '检查项目'},
        ),
        migrations.AlterModelOptions(
            name='checkproject',
            options={'verbose_name': '检查计划', 'verbose_name_plural': '检查计划'},
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='time',
            field=models.DateField(verbose_name='日期'),
        ),
    ]
