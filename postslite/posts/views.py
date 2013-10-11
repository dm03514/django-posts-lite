from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from posts.forms import FullPostForm
from posts.models import Post


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
            return HttpResponseRedirect(new_post.get_absolute_url())
    else:
        form = FullPostForm()

    return render(request, 'create_post.html', {
        'form': form
    })


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
