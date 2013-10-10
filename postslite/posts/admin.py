from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'title', 'created_datetime')
admin.site.register(Post, PostAdmin)
