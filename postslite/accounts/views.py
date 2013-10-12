from django.views.generic import TemplateView

class AccountSignupView(TemplateView):
    template_name = 'accounts_signup.html'
