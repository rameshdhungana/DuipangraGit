from django.conf.urls import include, url
from django.contrib import admin
from pangra.views import (extraarguments,nestedarguments,projectcreate,projectupdate,defaultarguments,keywordarguments,year_archive,articles,multiple_decorators,
                          templateview,class_form,register,login,homepage,email,insert_bike,Myview,replyview,
                          EntryView,BlogView,FormTestView,FormsetFactoryView,
                          FormSetFactory,ModelBlogFormsetView,AjaxView,
                          CarAndTruck)
from pangra.views import *

project_patterns=[url(r'^create/$', projectcreate),
                  url(r'^update/$', projectupdate),

                  ]

urlpatterns = [
    # Examples:
    # url(r'^$', 'Duipangra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register),
    url(r'^login/$', login,name='login'),
    url(r'^$', homepage,name='homepage'),
    url(r'^email/$',email),
    url(r'^bikeform/$',insert_bike),
    url(r'^myview$',Myview.as_view(result='argument is passed form as_view ')),
    url(r'^about$',Myview.as_view()),
    url(r'^replyview$',replyview.as_view()),
    url(r'^class_form$',class_form.as_view()),
    url(r'^template_view$',templateview.as_view()),
    url(r'^multiple_decorators$',multiple_decorators.as_view()),

#url types
    url(r'^article/2005/03/$',articles),
    url(r'^article/([0-9]{4})/([0-4]{2})',year_archive),
    url(r'^article/([0-9]{4})/([0-9]{2})/$',year_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/$', month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', articles),
    url(r'^keywords/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', keywordarguments),
    url(r'^defaultarguments/', defaultarguments),
    url(r'^defaultarguments/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/',defaultarguments),

#include in django



    url(r'^project/(?P<num>)/', include(project_patterns)),
    # url(r'^project/', include([url(r'^create/$', projectcreate),
    #                            url(r'^update/$', projectupdate),
    #
    #               ])),




    # url(r'^project/', include('django_website.contact.urls')),
    # url(r'^contact/', include('django_website.contact.urls')),

    #nested argument in url
    url(r'^nestedarguments/(?:page-(?P<num>\d+))/$', nestedarguments), # name followed by ?: but variable followed by ?P<>

    # pass extra arguments
    url(r'^extraarguments/', extraarguments,{'num':'199999'}),

    #enrty url
    url(r'^entry/$',EntryView.as_view(),name='entry'),
    #blog form ajax check
     url(r'^blog/$',BlogView.as_view(),name='blog'),

    #working with form errors
    url(r'^formtest/$', FormTestView.as_view(), name='formtest'),
    #formset  factory example
    url(r'^formsetfactory/$', FormSetFactory, name='formsetfactory'),
    #modelform formset
    url(r'^modelformset/$', ModelBlogFormsetView, name='modelformset'),

    #url for trucks and cars
    url(r'^carandtruck/$', CarAndTruck.as_view(), name='car_and_truck'),

    #working with ajax
    url(r'^ajax/$', AjaxView.as_view(), name='ajax'),
    url(r'^check_username/(?P<username>[\w\-]+)/$', UsernameValidation.as_view(), name='check_username'),

     #json ajax url
    url(r'^json/$',JsonAjax.as_view()),
    #ajaxpost exampole
    url(r'^postajax/$',Postajaxexample.as_view(),name = 'postajax'),

    #rest framework url
    url(r'^restframework/$', pygments_examples.as_view()),

    url(r'^pangra-api/', include('pangra_api.urls')),


]





