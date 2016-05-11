# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(max_length=100)),
                ('player_name', models.CharField(max_length=100)),
                ('rank_score', models.FloatField(default=1000.0)),
                ('wins', models.IntegerField(default=0)),
                ('loss', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('rank', models.IntegerField()),
                ('last_rank', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
