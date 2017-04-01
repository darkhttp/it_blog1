# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20170317_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_news', models.CharField(max_length=64, verbose_name='Тип новости')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Type_news', verbose_name='Тип новости'),
            preserve_default=False,
        ),
    ]
