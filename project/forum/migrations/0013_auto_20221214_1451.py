# Generated by Django 2.2.19 on 2022-12-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20221214_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]