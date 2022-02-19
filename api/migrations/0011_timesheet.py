# Generated by Django 4.0 on 2022-02-18 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0010_remove_user_region_alter_user_card_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('am', models.IntegerField(default=20)),
                ('pm', models.IntegerField(default=20)),
                ('check_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.checkreport')),
            ],
        ),
    ]
