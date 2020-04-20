from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include,url
from apps.user import views
app_name = 'user'
urlpatterns = [
    url(r'register/$', views.RegisterView.as_view(), name='register'), #注册
    url(r'active/(.*)/$', views.ActiveView.as_view(), name='active'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),  # 注销登录
    url(r'^$', views.UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    url(r'^order/(?P<page>\d+)/$', views.UserOrderView.as_view(), name='order'), # 用户中心-订单页
    # url(r'^order/$', views.UserOrderView.as_view(), name='order'), # 用户中心-订单页
    url(r'^address/$', views.AddressView.as_view(), name='address'), # 用户中心-地址页
]