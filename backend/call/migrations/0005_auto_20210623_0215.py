# Generated by Django 3.2.4 on 2021-06-23 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('call', '0004_alter_call_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='call_users', to=settings.AUTH_USER_MODEL, verbose_name='atendente'),
        ),
        migrations.AlterField(
            model_name='call',
            name='status',
            field=models.CharField(choices=[('a', 'Aberto'), ('b', 'Em andamento'), ('c', 'Concluído')], default='a', max_length=1, verbose_name='status'),
        ),
    ]
