from django.db import models
from django.contrib.auth.models import User


class ChatGroup(models.Model):
    name = models.CharField(max_length=255)

    users = models.ManyToManyField(
        User,
        through='ChatGroupMember',
        related_name='chat_groups'
    )

    def __str__(self):
        return self.name


class ChatGroupMember(models.Model):
    chat_group = models.ForeignKey(
        ChatGroup,
        on_delete=models.CASCADE,
        related_name='members'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_memberships'
    )

    def __str__(self):
        return f'Chat membership {self.user} -> {self.chat_group}'
