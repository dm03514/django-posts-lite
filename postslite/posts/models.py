from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Sum
from django.utils.text import slugify

from posts.managers import PostOrderManager


class Post(models.Model):
    created_by = models.ForeignKey(User)
    created_datetime = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=256)

    objects = PostOrderManager()

    def get_upvote_url(self):
        """
        Returns the url required to upvote this post.
        """
        return reverse('posts:vote', args=[str(self.pk), 'up'])

    def get_downvote_url(self):
        """
        Returns the url required to downvote this post.
        """
        return reverse('posts:vote', args=[str(self.pk), 'down'])

    def get_vote_score(self):
        """
        Returns a post rating.
        """
        q = PostVote.objects.filter(post=self).aggregate(Sum('score'))
        return q['score__sum'] if q['score__sum'] else 0

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.pk)])

    def get_disqus_id(self):
        """
        Returns unique identifier used in disqus.
        @return string
        """
        return '{}_post_{}'.format(self.pk, slugify(self.title))

    def clean(self):
        """
        Ensures that user has provided either a `link` AND/OR a `text` value.
        """
        if not self.link and not self.text:
            raise ValidationError('Must include a link AND/OR a text value')

    def __unicode__(self):
        """
        Displays human readable representation.
        """
        return '{} - {}'.format(self.pk, self.title)


class PostVote(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True)
    score = models.IntegerField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return '{} - {}'.format(self.score, self.post.title)

    class Meta:
        unique_together = ('post', 'created_by')
    
