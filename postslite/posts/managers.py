from django.db import models
from django.db.models import Sum


class PostOrderManager(models.Manager):

    def get_query_set(self):
        """
        Override to order by the ordering.
        """
        return super(PostOrderManager, self).get_query_set().annotate(
            vote_score=Sum('postvote__score')).order_by('-vote_score')
    
