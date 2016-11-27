# -*- coding:utf8 -*-
"""
Project URL Configuration
"""
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from frontend import views

urlpatterns = [
    url(r'^api/provider-check/(?P<provider>[\w]+)/(?P<car_id>[\w]+)/(?P<certificate_id>[\w]+)', views.ProviderCheck.as_view()),
    url(r'^$', views.FrontPage.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
