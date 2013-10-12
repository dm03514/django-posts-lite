from django.conf.urls import patterns, url

from accounts.views import AccountSignupView


urlpatterns = patterns('',
    url(r'^signup/$', AccountSignupView.as_view(), name="signup"),
)
