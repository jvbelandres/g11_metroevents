# Generated by Django 3.1.1 on 2021-03-23 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notif_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 23, 18, 24, 47, 617359)),
        ),
    ]
