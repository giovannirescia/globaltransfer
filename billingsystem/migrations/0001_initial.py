# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.IntegerField(max_length=70, unique=True, serialize=False, primary_key=True)),
                ('cost', models.IntegerField()),
                ('bill_type', models.CharField(max_length=1)),
                ('billed_date', models.DateTimeField(verbose_name=b'date billed')),
                ('paid_date', models.DateTimeField(null=True, verbose_name=b'date paid')),
                ('paid', models.BooleanField(default=False)),
                ('payment_type', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('taxi_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bill',
            name='taxi_id',
            field=models.ForeignKey(to='billingsystem.Taxi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
