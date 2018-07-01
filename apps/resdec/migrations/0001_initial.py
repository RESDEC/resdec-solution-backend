# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-07 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='VariabilityEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='VariabilityEnvironmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('path', models.CharField(default=b'', max_length=80)),
                ('extension', models.CharField(max_length=4)),
                ('size', models.IntegerField(default=0)),
                ('number_records', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to=b'reosurces/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('relationship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resdec.RelationshipType')),
                ('variability_environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resdec.VariabilityEnvironment')),
            ],
        ),
    ]