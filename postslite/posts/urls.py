from django.conf.urls import patterns, url

from posts.views import PostListView


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name="list_posts"),
    url(r'^post/create/$', 'posts.views.create_post', name="create_post"),
    url(r'^post/post/(?P<post_id>\d+)/$', 'posts.views.display_post', name="display_post"),
)
