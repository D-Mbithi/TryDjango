from django.contrib import admin
from .models import Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'user', 'comment']
    list_filter = ('user',)


admin.site.register(Comment, CommentAdmin)
