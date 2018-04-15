from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_post, name='list_post'),
    url(r'^create$', views.create_post, name='create_post'),
    url(r'^update$', views.update_post, name='update_post'),
    url(r'^delete$', views.delete_post, name='delete_post'),
    url(r'^detail$', views.detail_post, name='detail_post'),
]
