# Generated by Django 2.2.12 on 2020-06-21 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200620_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
