# Generated by Django 3.2.4 on 2021-06-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0006_auto_20210623_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='category',
        ),
    ]
