from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from posts.forms import FullPostForm


def list_posts(request):
    """
    Lists all posts, ordered by rating desc / datetime created desc.
    """
    pass


@login_required
def create_post(request):
    """
    Create a post (POST) or render a form (GET) to create a post, 
    depending on the request type.
    """
    if request.method == 'POST':
        form = FullPostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = FullPostForm()

    return render(request, 'create_post.html', {
        'form': form
    })

