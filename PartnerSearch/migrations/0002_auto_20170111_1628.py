# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-11 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PartnerSearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitrequest',
            name='deadline_call',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>DD-MM-YYYY</em>.', null=True),
        ),
        migrations.AddField(
            model_name='submitrequest',
            name='type_of_partners',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='submitrequest',
            name='interest_Expected',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>DD-MM-YYYY</em>.', null=True),
        ),
        migrations.AlterField(
            model_name='submitrequest',
            name='summary',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
