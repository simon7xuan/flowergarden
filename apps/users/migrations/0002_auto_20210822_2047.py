# Generated by Django 2.2 on 2021-08-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='head_image/default.jpg', upload_to='head_image/%Y/%m', verbose_name='用户头像'),
        ),
    ]
