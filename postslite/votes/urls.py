from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^vote/(?P<key>\w+)/(?P<object_id>\d+)/(?P<vote_type>\w+)/$', 
        'votes.views.create_vote', name="create_vote"),
)
