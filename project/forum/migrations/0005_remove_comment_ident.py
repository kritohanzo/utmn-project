# Generated by Django 2.2.19 on 2022-12-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_comment_ident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ident',
        ),
    ]
