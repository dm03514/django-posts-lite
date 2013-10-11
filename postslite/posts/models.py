from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Sum

from votes.models import Vote


class Post(models.Model):
    created_by = models.ForeignKey(User)
    created_datetime = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=256)

    def get_upvote_url(self):
        """
        Returns the url required to upvote this post.
        """
        return reverse('votes:create_vote', args=['post', str(self.pk), 'up'])

    def get_downvote_url(self):
        """
        Returns the url required to downvote this post.
        """
        return reverse('votes:create_vote', args=['post', str(self.pk), 'down'])

    def get_vote_score(self):
        """
        Returns a post rating.
        """
        q = Vote.objects.filter(key='post', object_id=self.pk).aggregate(Sum('score'))
        return q['score__sum'] if q['score__sum'] else 0

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.pk)])

    def __unicode__(self):
        """
        Displays human readable representation.
        """
        return '{} - {}'.format(self.pk, self.title)
