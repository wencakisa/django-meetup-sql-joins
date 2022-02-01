# Generated by Django 4.0.2 on 2022-02-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatgroupmember_remove_chatgroup_members_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='chatgroupmember',
            constraint=models.UniqueConstraint(fields=('chat_group', 'user'), name='unique_chat_group_user'),
        ),
    ]
