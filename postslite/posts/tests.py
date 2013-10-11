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

    def test_vote_order_by_success(self):
        """
        Tests that posts can be ordered by their votes.
        """
        # create 2 posts
        post_one = Post(created_by=self.test_user, text='asdfasdf', title='post1')
        post_one.save()
        post_two = Post(created_by=self.test_user, text='asdfasdf', title='post2')
        post_two.save()
        post_three = Post(created_by=self.test_user, text='asdfasdf', title='post3')
        post_three.save()
        # give post_one a vote so it should show up first in ordering
        vote = PostVote(created_by=self.test_user, score=1, post=post_one)
        vote.save()
        vote = PostVote(created_by=self.test_user, score=-1, post=post_three)
        vote.save()
        # get ordering order should be post_one, post_two, post_three
        # this should fail becuase an int comes Before None value in the order by function!
        posts = Post.objects.all()
        self.assertEqual([post.pk for post in posts], [1, 2, 3])
        #import ipdb; ipdb.set_trace();
