# Generated by Django 2.2.5 on 2020-02-09 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_auto_20200209_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_no',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='room number must be of form: A-9', regex='^([A-Z])-([0-9])+$')]),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('room_no', 'hostel')},
        ),
    ]
