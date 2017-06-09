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
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title = 'Pastebin API')

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

	#======== for coreapi scheme ==========

	url(r'^schema/$', schema_view),

	#======== for snippets =============

	url(r'^snippets/$', snippet_list, name='snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),

	#======== for users ==============

	url(r'^users/$', user_list, name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),	
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# =================== USING ROUTERS =======================
'''
Because we're using ViewSet classes rather than View classes, we actually don't need to design the URL conf ourselves. 
The conventions for wiring up resources into views and urls can be handled automatically, using a Router class. 
'''

# from django.conf.urls import url, include
# from snippets import views
# from rest_framework.routers import DefaultRouter

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# # The API URLs are now determined automatically by the router.
# # Additionally, we include the login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]