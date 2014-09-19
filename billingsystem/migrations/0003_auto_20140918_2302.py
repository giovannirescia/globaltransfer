# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystem', '0002_auto_20140918_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='cost_cash',
            new_name='total_cash',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='cost_credit_card',
            new_name='total_credit_card',
        ),
    ]
