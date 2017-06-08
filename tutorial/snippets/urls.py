from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	# url(r'^snippets/$', views.snippet_list),
	# url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

	url(r'^snippets/$', views.SnippetList.as_view())
	url(r'^snippets/(?P<pk>[0-9]+)/$)', views.SnippetDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)