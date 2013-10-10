from django.forms import ModelForm

from posts.models import Post


class FullPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('link', 'text', 'title')
