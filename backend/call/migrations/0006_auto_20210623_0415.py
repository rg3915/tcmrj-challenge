# Generated by Django 3.2.4 on 2021-06-23 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0005_auto_20210623_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='call.category', verbose_name='categoria'),
        ),
        migrations.AddField(
            model_name='call',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='call.subcategory', verbose_name='subcategoria'),
        ),
    ]
