# Generated by Django 4.1.5 on 2023-02-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
