# Generated by Django 2.2.1 on 2019-05-12 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengtou', '0003_auto_20190512_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advware',
            old_name='adv_id',
            new_name='adv',
        ),
        migrations.RenameField(
            model_name='commonproblem',
            old_name='user_id',
            new_name='user',
        ),
    ]
