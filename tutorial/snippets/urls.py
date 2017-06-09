from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#====================== WHILE USING VIEWS ==========================================

# urlpatterns = [
# 	# root of API
# 	url(r'^$', views.api_root),

# 	#======== for snippets =============

# 	# url(r'^snippets/$', views.snippet_list),
# 	# url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

# 	url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
# 	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
# 	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

# 	#======== for users ==============

# 	url(r'^users/$', views.UserList.as_view(), name='user-list'),
# 	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),	
# ]

# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

#===========================BIND USING VIEWSETS======================================

from snippets.views import UserViewSet, SnippetViewSet, api_root
from rest_framework import renderers


snippet_list = SnippetViewSet.as_view({
	'get': 'list',
	'post': 'create',
	})

snippet_detail = SnippetViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
	})

snippet_highlight = SnippetViewSet.as_view({
	'get': 'highlight',
	}, renderer_classes = [renderers.StaticHTMLRenderer,])

user_list = UserViewSet.as_view({
	'get': 'list',
	})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
	url(r'^$', api_root),

	#======== for snippets =============

	url(r'^snippets/$', snippet_list, name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_highlight, name='snippet-highlight'),

	#======== for users ==============

	url(r'^users/$', user_list, name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),	
]

