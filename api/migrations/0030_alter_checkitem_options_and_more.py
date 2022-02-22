# Generated by Django 4.0 on 2022-02-19 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_checkitem_check_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkitem',
            options={'verbose_name': '门诊预约单', 'verbose_name_plural': '门诊预约单'},
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='check_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.checkproject', verbose_name='门诊预约单'),
        ),
    ]
