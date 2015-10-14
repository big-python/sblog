from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$','sblog.apps.login.views.login',name='login'),
    url(r'^login/$','sblog.apps.login.views.login',name='login'),
    url(r'^doLogin/$','sblog.apps.login.views.doLogin',name='doLogin'),
    url(r'^reg/$','sblog.apps.login.views.reg',name='reg'),
    url(r'^doReg/$','sblog.apps.login.views.doReg',name='doReg'),
)
