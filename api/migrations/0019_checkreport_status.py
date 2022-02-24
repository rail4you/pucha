# Generated by Django 4.0 on 2022-02-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0018_remove_checkreport_checkitem_checkitem_check_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkreport',
            name='status',
            field=models.CharField(choices=[('报告已完成', 'Finished'), ('报告未填写', 'Unfinished')], default='Unfinished',
                                   max_length=50),
        ),
    ]
