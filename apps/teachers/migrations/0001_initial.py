# Generated by Django 2.2 on 2021-08-22 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='教师名')),
                ('points', models.CharField(max_length=50, verbose_name='教学特点')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('image', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像')),
            ],
            options={
                'verbose_name': '授课教师',
                'verbose_name_plural': '授课教师',
            },
        ),
    ]
