# Generated by Django 4.0 on 2022-02-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
