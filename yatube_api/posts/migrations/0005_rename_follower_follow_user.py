# Generated by Django 3.2.16 on 2023-07-19 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='user',
        ),
    ]