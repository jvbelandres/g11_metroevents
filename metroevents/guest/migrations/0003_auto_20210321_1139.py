# Generated by Django 3.1.4 on 2021-03-21 03:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_auto_20210321_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 21, 11, 38, 59, 130180)),
        ),
        migrations.AlterModelTable(
            name='currentuser',
            table='currentUser',
        ),
    ]
