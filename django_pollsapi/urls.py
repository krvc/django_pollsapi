from django.conf.urls import include, url
from django.contrib import admin

import pollsapi.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_pollsapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', pollsapi.views.PollList.as_view()),
    url(r'poll/(?P<pk>[0-9]+)/$',pollsapi.views.PollDetail.as_view()),
    # url(r'^login/', pollsapi.views.Login.as_view()),

]
