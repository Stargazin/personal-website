# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def load_topics(apps, schema_editor):
	Topic = apps.get_model('blog', 'Topic')

	life = Topic(name='life')
	life.save()

	music = Topic(name='music')
	music.save()

	web = Topic(name='web')
	web.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(load_topics)
    ]
