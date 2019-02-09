# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-08 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextureChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('TOP', 'Top'), ('BOTTOM', 'Bottom'), ('BACK', 'Back'), ('NECK', 'Neck')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='TextureOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texture_option', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='texturechoice',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.TextureOption'),
        ),
    ]