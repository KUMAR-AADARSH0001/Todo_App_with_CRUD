# Generated by Django 4.1.5 on 2023-02-17 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todoapp_created_at_alter_todoapp_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 17, 10, 49, 1, 339108), editable=False),
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
