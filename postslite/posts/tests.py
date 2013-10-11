from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from posts.forms import FullPostForm
from posts.models import Post, PostVote


class PostsTest(TestCase):

    def setUp(self):
        """
        Called before every test.
        """
        self.username = 'test'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, None, self.password)

    def test_create_post_get_request_success(self):
        """
        Assert that the create_post.html template is loaded on a GET request.
        """
        self.client.login(username=self.username, 
                          password=self.password)
        response = self.client.get(reverse('posts:create_post'))
        self.assertTemplateUsed(response, 'create_post.html')
        self.assertIsInstance(response.context['form'], FullPostForm)
        #import ipdb; ipdb.set_trace();

    def test_votepost_create_success(self):
        """
        Tests that a new vote can successfully be created
        """
        self.client.login(username=self.username, 
                          password=self.password)
        # create a new post
        post = Post(created_by=self.test_user, text='asdfasdf', title='tests')
        post.save()
        response = self.client.post(reverse('posts:vote', 
                                            args=[post.pk, 'up']), 
                                    follow=True)
        self.assertTrue('Thank you for voting' in response.content)
        vote = PostVote.objects.get(post=post)
        self.assertEqual(vote.score, 1)
        #import ipdb; ipdb.set_trace();
