# Generated by Django 2.2.12 on 2020-06-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200621_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='user_id',
            field=models.CharField(max_length=30),
        ),
    ]