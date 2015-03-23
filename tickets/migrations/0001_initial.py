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
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date', auto_now_add=True)),
                ('last_update', models.DateTimeField(verbose_name='Date', auto_now=True)),
                ('subject', models.CharField(verbose_name='Subject', max_length=255)),
                ('description', models.TextField(help_text='A detailed description of your problem.', verbose_name='Description')),
                ('status', models.SmallIntegerField(verbose_name='Status', default=0, choices=[(0, 'New'), (1, 'Feedback'), (3, 'In Progress'), (4, 'Resolved'), (5, 'Closed')])),
                ('assignee', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='assigned_tickets', blank=True, verbose_name='Assignee')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Creator', related_name='tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date', auto_now_add=True)),
                ('comment', models.TextField(verbose_name='Comment')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('ticket', models.ForeignKey(to='tickets.Ticket', verbose_name='Ticket', related_name='comments')),
            ],
            options={
                'verbose_name': 'Ticket comment',
                'ordering': ['date'],
                'verbose_name_plural': 'Ticket comments',
            },
            bases=(models.Model,),
        ),
    ]
