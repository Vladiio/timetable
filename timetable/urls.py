from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^get_mark/$', views.get_mark, name='get_mark'),
)
