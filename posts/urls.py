from django.conf.urls import url
from .views import get_post, create_edit_post, post_detail

urlpatterns = [
    url(r'^$', get_post, name='get_posts' ),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_edit_post, name='edit_post')
    ]