from django.conf.urls.defaults import *

urlpatterns = patterns('subscription.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)
