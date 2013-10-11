from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from votes.models import Vote


class VotesTest(TestCase):

    def setUp(self):
        """
        Called before every test.
        """
        self.username = 'test'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, None, self.password)

    def test_vote_create_success(self):
        """
        Tests that a new vote can successfully be created
        """
        self.client.login(username=self.username, 
                          password=self.password)
        vote_key = 'post'
        vote_object_id = 1
        response = self.client.post(reverse('votes:create_vote', 
                                            args=[vote_key, vote_object_id, 'up']), 
                                    follow=True)
        self.assertTrue('Thank you for voting' in response.content)
        vote = Vote.objects.get(key=vote_key, object_id=vote_object_id, 
                                created_by=self.test_user)
        self.assertEqual(vote.score, 1)
        #import ipdb; ipdb.set_trace();
