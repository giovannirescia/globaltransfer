# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='taxi_id',
            new_name='taxi',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='cost',
        ),
        migrations.AddField(
            model_name='bill',
            name='cost_cash',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='cost_credit_card',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
