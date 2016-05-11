# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['-rank_score']},
        ),
        migrations.AddField(
            model_name='club',
            name='rank_difference',
            field=models.CharField(default=b'-', max_length=20),
            preserve_default=True,
        ),
    ]
