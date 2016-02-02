# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(unique=True)),
                ('title_url', models.TextField(blank=True)),
                ('number', models.TextField(unique=True)),
                ('date', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('review', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.TextField()),
                ('heading', models.TextField()),
                ('content', models.TextField()),
                ('post', models.ForeignKey(related_name='sections', to='blog.Post')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(related_name='posts', to='blog.Topic'),
        ),
    ]
