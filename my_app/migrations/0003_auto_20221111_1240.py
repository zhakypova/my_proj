# Generated by Django 3.2 on 2022-11-11 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20221111_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='the_json',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='the_json',
        ),
        migrations.RemoveField(
            model_name='work',
            name='the_json',
        ),
    ]
