from django.contrib import admin
from .models import *

# Register your models here.
class Messages(admin.ModelAdmin):
    list_display =('message', 'author', 'authoredDate', 'seenDate', 'readed', 'readBy', 'authorizedTo')
    filter_by = ('authoredDate', 'seenDate', 'readed', 'readBy', 'authorizedTo')
    ordering = ('author', 'authoredDate', 'seenDate',)

class Replies(admin.ModelAdmin):
    list_display = ('message', 'replyTo', 'repliedBy', 'repliedDate', 'main_message')
    filter_by = ('replyTo', 'repliedBy', 'repliedDate')
    ordering = ('repliedDate',)


admin.site.register(MessageTable, Messages)
admin.site.register(ReplyTable, Replies)
