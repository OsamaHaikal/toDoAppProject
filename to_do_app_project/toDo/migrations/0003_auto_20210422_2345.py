# Generated by Django 3.1.7 on 2021-04-22 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0002_auto_20210422_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='userCreater',
            new_name='user',
        ),
    ]
