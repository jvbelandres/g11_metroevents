# Generated by Django 3.1.4 on 2021-03-22 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0004_auto_20210322_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 22, 20, 8, 54, 885394)),
        ),
    ]