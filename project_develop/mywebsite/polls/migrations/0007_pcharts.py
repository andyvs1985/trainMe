# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150916_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='pcharts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=200)),
                ('user_inputs', models.ForeignKey(to='polls.Answer')),
            ],
        ),
    ]
