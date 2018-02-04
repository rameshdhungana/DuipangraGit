from django.conf.urls import url
from pangra_api import views
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),

    url(r'^snippets-api/$', views.snippet_api_list),
    url(r'^snippets-api/(?P<pk>[0-9]+)$', views.snippet_api_detail),

    url(r'^snippets-class/$', views.SnippetList.as_view()),
    url(r'^snippets-class/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),

    url(r'^snippets-mixin/$', views.SnippetList.as_view()),
    url(r'^snippets-mixin/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),

    url(r'^snippets-generic/$', views.SnippetGenericList.as_view()),
    url(r'^snippets-generic/(?P<pk>[0-9]+)$', views.SnippetGenericDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)