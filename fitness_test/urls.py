# coding: utf-8
"""fitness_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app.views import DoctorList, ReceptionView

urlpatterns = [
    url(r'^$', DoctorList.as_view(), name='start'),
    url(r'^doctor/(?P<doctor_id>\d+)/$',ReceptionView.as_view(), name='reception'),
    url(r'^date_from_ajax/$', 'app.views.date_from_ajax', name='date_from_ajax'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog')
]
