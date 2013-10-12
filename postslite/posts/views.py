from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from posts.forms import FullPostForm
from posts.models import Post, PostVote


@login_required
def create_post(request):
    """
    Create a post (POST) or render a form (GET) to create a post, 
    depending on the request type.
    """
    if request.method == 'POST':
        form = FullPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.created_by = request.user
            new_post.save()
            # creating a PostVote of 0,
            # A PostVote is created here and initialized to 0 so that the ordering
            # works correctly...
            # This might be better off as a signal
            vote = PostVote(created_by=request.user, score=0, post=new_post)
            vote.save()
            return HttpResponseRedirect(new_post.get_absolute_url())
    else:
        form = FullPostForm()

    return render(request, 'create_post.html', {
        'form': form
    })


@login_required
def vote(request, post_id, vote_type):
    """
    Creates a new PostVote object, and persists it to DB.
    Redirects user back to referer page.
    """
    valid_vote_types = ('up', 'down')
    if vote_type not in valid_vote_types:
        messages.add_message(request, messages.INFO, 'Invalid vote type')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    # make sure that this is a valid post_id
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.add_message(request, messages.INFO, 'Invalid post_id')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        
    score = 1 if (vote_type == 'up') else -1
    # if this user has already attempted to cast a vote for this key/object_id
    # will throw integrity error, gloss over this for right now
    try:
        new_vote = PostVote(score=score, post=post, created_by=request.user)
        new_vote.save()
    except IntegrityError:
        pass
    
    messages.add_message(request, messages.INFO, 'Thank you for voting')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


class PostDetailView(DetailView):
    """
    Display an individual post.
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostListView(ListView):
    """
    Lists all posts, ordered by rating desc / datetime created desc.
    """
    model = Post
    template_name = 'post_list.html'
    paginate_by = 10
    context_object_name = 'post_list'
