# Generated by Django 2.2.19 on 2022-12-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_auto_20221214_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=420, verbose_name='Текстs'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=42, verbose_name='Заголовокs'),
        ),
    ]
