from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    (r'^$', RedirectView.as_view(url='/posts/')),
    
    url(r'^login/$', 'django.contrib.auth.views.login', {
            'template_name': 'login.html'
    }, name='login'),
)
