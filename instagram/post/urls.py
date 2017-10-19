from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/create/$', views.post_create, name='post_create'),
    url(r'^post/(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_pk>\d+)/comment/create/$', views.comment_create, name='comment_create'),
]
