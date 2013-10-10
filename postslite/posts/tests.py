from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from posts.forms import FullPostForm


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

