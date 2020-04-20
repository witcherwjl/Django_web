from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from apps.goods import views
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'index/$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'index/$', views.index, name='index'),
]