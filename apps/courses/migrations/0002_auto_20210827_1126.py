# Generated by Django 2.2 on 2021-08-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '课程章节', 'verbose_name_plural': '课程章节'},
        ),
        migrations.AddField(
            model_name='course',
            name='notice',
            field=models.CharField(default='', max_length=300, verbose_name='课程公告'),
        ),
    ]
