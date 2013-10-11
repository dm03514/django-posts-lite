from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect

from votes.models import Vote


@login_required
def create_vote(request, key, object_id, vote_type):
    """
    Creates a new vote object, and persists it to DB.
    Redirects user back to referer page.
    """
    valid_vote_types = ('up', 'down')
    if vote_type not in valid_vote_types:
        messages.add_message(request, messages.INFO, 'Invalid vote type')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    score = 1 if (vote_type == 'up') else -1
    # if this user has already attempted to cast a vote for this key/object_id
    # will throw integrity error, gloss over this for right now
    try:
        new_vote = Vote(score=score, key=key, object_id=object_id, created_by=request.user)
        new_vote.save()
    except IntegrityError:
        pass
    
    messages.add_message(request, messages.INFO, 'Thank you for voting')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
