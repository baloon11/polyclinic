# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('specialization', models.CharField(max_length=300, verbose_name='Специализация')),
                ('info', models.CharField(max_length=10000, verbose_name='Инфо о враче')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Дата приема ')),
                ('time', models.CharField(max_length=5, verbose_name='Время приема ')),
                ('patient_name', models.CharField(max_length=300, verbose_name='ФИО ')),
                ('patient_info', models.CharField(max_length=10000, verbose_name='Инфо о пациенте ')),
                ('doctor', models.ForeignKey(verbose_name='Доктор ', to='app.Doctor')),
            ],
            options={
                'verbose_name': 'Прием',
                'verbose_name_plural': 'Приемы',
            },
        ),
    ]
