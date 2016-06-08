# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_pcharts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pcharts',
            name='user_inputs',
        ),
        migrations.AddField(
            model_name='question',
            name='Age',
            field=models.IntegerField(default=34, verbose_name=22),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Height',
            field=models.FloatField(default=5.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Name',
            field=models.CharField(default='Anand', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='Weight',
            field=models.FloatField(default=56),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='pcharts',
        ),
    ]
