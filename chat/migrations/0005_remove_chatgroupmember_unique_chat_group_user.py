# Generated by Django 4.0.2 on 2022-02-21 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chatgroupmember_unique_chat_group_user'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='chatgroupmember',
            name='unique_chat_group_user',
        ),
    ]
