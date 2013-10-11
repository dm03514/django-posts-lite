from django.conf.urls import patterns, url

from posts.views import PostDetailView, PostListView


urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name="list_posts"),
    url(r'^post/create/$', 'posts.views.create_post', name="create_post"),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_detail"),
)
