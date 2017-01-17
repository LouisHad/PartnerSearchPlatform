# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-16 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PartnerSearch', '0004_submitrequest_pic_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Interest',
            new_name='UserInterestTo',
        ),
        migrations.AddField(
            model_name='submitrequest',
            name='type_of_Submit',
            field=models.CharField(choices=[('R', 'Request'), ('I', 'Interest')], default='I', max_length=2),
        ),
    ]