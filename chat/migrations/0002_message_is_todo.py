# Generated by Django 3.1.4 on 2020-12-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_todo',
            field=models.BooleanField(default=False, verbose_name='is_todo'),
        ),
    ]
