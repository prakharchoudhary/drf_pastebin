from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	# root of API
	url(r'^$', views.api_root),

	#======== for snippets =============

	# url(r'^snippets/$', views.snippet_list),
	# url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

	url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

	#======== for users ==============

	url(r'^users/$', views.UserList.as_view(), name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),	
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)