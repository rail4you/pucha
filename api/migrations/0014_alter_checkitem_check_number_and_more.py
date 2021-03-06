# Generated by Django 4.0 on 2022-02-18 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0013_alter_checkproject_options_alter_checkreport_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkitem',
            name='check_number',
            field=models.IntegerField(verbose_name='检查编号'),
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='check_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.checkproject',
                                    verbose_name='检查项目'),
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='check_report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.checkreport',
                                    verbose_name='检查报告'),
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='check_time',
            field=models.DateTimeField(null=True, verbose_name='检查时间'),
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check_doctor',
                                    to='api.user', verbose_name='检查医生'),
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check_user',
                                    to='api.user', verbose_name='检查用户'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='announcement',
            field=models.TextField(verbose_name='通知'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='check_agent',
            field=models.TextField(verbose_name='检查机构'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='check_item',
            field=models.TextField(null=True, verbose_name='检查项目'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user', verbose_name='联系人'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='credit',
            field=models.IntegerField(null=True, verbose_name='项目份额'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='department_name',
            field=models.TextField(verbose_name='部门名称'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='department_position',
            field=models.TextField(verbose_name='部门位置'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='end_time',
            field=models.DateTimeField(verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='name',
            field=models.CharField(max_length=20, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='checkproject',
            name='start_time',
            field=models.DateTimeField(verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='checkreport',
            name='name',
            field=models.CharField(max_length=50, verbose_name='检查报告名称'),
        ),
        migrations.AlterField(
            model_name='checkreport',
            name='result',
            field=models.TextField(verbose_name='检查结果'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='am',
            field=models.IntegerField(default=20, verbose_name='上午访问人数'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='check_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.checkproject',
                                    verbose_name='检查项目'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='is_holiday',
            field=models.BooleanField(default=False, verbose_name='是否是节假日'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='pm',
            field=models.IntegerField(default=20, verbose_name='下午访问人数'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='time',
            field=models.DateField(verbose_name='检查日'),
        ),
    ]
