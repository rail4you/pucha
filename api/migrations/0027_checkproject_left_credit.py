# Generated by Django 4.0 on 2022-02-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0026_region_left_credit_alter_checkreport_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkproject',
            name='left_credit',
            field=models.IntegerField(null=True, verbose_name='剩余份额'),
        ),
    ]
