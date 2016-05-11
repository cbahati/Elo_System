# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clubs.models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20151220_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_image',
            field=models.ImageField(default=b'Elo_System/static/static_dirs/img/club_banners/deault.jpg', null=True, upload_to=clubs.models.get_image_path, blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='goal_against',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club',
            name='goal_difference',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club',
            name='goal_for',
            field=models.IntegerField(default=0),
        ),
    ]
