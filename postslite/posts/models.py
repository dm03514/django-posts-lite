from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    created_by = models.ForeignKey(User)
    created_datetime = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('display_post', args=[str(self.pk)])

    def __unicode__(self):
        """
        Displays human readable representation.
        """
        return '{} - {}'.format(self.pk, self.title)
