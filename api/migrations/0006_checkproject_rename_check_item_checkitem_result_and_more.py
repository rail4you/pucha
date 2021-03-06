# Generated by Django 4.0 on 2022-02-17 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0005_checkitem_region_remove_checkreport_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('department_name', models.TextField()),
                ('department_position', models.TextField()),
                ('check_agent', models.TextField()),
                ('check_item', models.TextField(null=True)),
                ('announcement', models.TextField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.RenameField(
            model_name='checkitem',
            old_name='check_item',
            new_name='result',
        ),
        migrations.RemoveField(
            model_name='checkitem',
            name='announcement',
        ),
        migrations.RemoveField(
            model_name='checkitem',
            name='check_agent',
        ),
        migrations.RemoveField(
            model_name='checkitem',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='checkitem',
            name='department_position',
        ),
        migrations.RemoveField(
            model_name='checkitem',
            name='name',
        ),
        migrations.AddField(
            model_name='checkitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check_user',
                                    to='api.user'),
        ),
        migrations.AlterField(
            model_name='checkitem',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_doctor',
                                    to='api.user'),
        ),
        migrations.DeleteModel(
            name='CheckReport',
        ),
        migrations.AddField(
            model_name='checkitem',
            name='check_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.checkproject'),
        ),
    ]
