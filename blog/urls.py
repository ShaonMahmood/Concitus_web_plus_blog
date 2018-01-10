from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views


urlpatterns = [
    url(r'^(?:page-(?P<pagenum>[0-9-\w]+))?$', views.post_list, name='post_list'),

    url(r'^post/(?P<pk>\d+)/(?P<slug>[-\w]+)/$',
        #r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^tagsearch/(?P<pk>[0-9.\w]+)/(?:page-(?P<pagenum>[0-9-\w]+))?$', views.tag_search, name='tagSearch'),
    url(r'^writersearch/(?P<writer>[0-9.\w]+)/(?:page-(?P<pagenum>[0-9-\w]+))?$', views.search_by_writer, name='writersearch'),
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search,name='searchBlog'),

    #url(r'^login/$', views.user_login, name='login'),

    url(r'^login/$', login,name='login'),
    url(r'^logout/$', logout,{'next_page': '/blog'},name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]