# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-24 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program_enrollments', '0002_historicalprogramcourseenrollment_programcourseenrollment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='programenrollment',
            unique_together=set([('user', 'external_user_key', 'program_uuid', 'curriculum_uuid')]),
        ),
    ]
