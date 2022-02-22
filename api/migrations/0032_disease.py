# Generated by Django 4.0 on 2022-02-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_checkitem_check_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.TextField()),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': '疾病',
                'verbose_name_plural': '疾病',
            },
        ),
    ]
