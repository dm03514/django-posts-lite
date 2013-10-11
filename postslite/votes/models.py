from django.contrib.auth.models import User
from django.db import models


class Vote(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    created_by = models.ForeignKey(User)
    key = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    class Meta:
        unique_together = ('key', 'object_id', 'created_by')

    def __unicode__(self):
        return '{} - {}'.format(self.model_name, self.score)
