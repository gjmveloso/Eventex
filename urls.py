from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^$', homepage, name="home"),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')), 
    # Example:
    # (r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('core.views',
    url(r'^palestrante/([-\w]+)/$', 'speaker', name='speaker'),
    url(r'^palestras/$', 'talks', name='talks'),)
