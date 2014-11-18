from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^project/(?P<project_id>\d+)/$', views.project, name='project'),
	url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
)
