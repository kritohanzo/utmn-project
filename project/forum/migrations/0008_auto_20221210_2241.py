# Generated by Django 2.2.19 on 2022-12-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=14, verbose_name='Заголовок'),
        ),
    ]