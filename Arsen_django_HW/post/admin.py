from django.contrib import admin
from . models import Post, Tag, Category, Comment


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'content', 'rate', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)