from django.contrib import admin

from chat.models import Chat, ChatMessage


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    search_fields = ("id", "title")


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    autocomplete_fields = ("chat",)
