# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_question_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='email',
            new_name='my_mail',
        ),
    ]
