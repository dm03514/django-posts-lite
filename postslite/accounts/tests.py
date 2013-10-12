from django.core.urlresolvers import reverse
from django.test import TestCase


class AccountsTest(TestCase):

    def test_get_account_signup_page(self):
        """
        Tests the accounts_signup template is loaded on signup page request.
        """
        response = self.client.get(reverse('accounts:signup'))
        self.assertTemplateUsed(response, 'accounts_signup.html')
