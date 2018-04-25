from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_post, name='list'),
    url(r'^create$', views.create_post, name='create'),
    url(r'^(?P<pk>\d+)/$', views.detail_post, name='detail'),
    url(r'^(?P<pk>\d+)/update$', views.update_post, name='update'),
    url(r'^(?P<pk>\d+)/delete$', views.delete_post, name='delete'),
]
