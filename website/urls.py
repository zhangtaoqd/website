from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^App/', include(admin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
)