from django.contrib import admin
from posts.models import Post, PostVote


class PostAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'title', 'created_datetime')
admin.site.register(Post, PostAdmin)

class PostVoteAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'post', 'score', 'created_datetime')
admin.site.register(PostVote, PostVoteAdmin)
