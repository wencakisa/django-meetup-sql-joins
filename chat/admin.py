from django.contrib import admin

from chat.models import ChatGroup, ChatGroupMember


class MembersInline(admin.StackedInline):
    model = ChatGroupMember


@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    inlines = (MembersInline, )
