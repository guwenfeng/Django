from django.conf.urls import url

from  . import views
from  .connterllos import typography,base


urlpatterns = [
    url(r'^index', base.index, name='index'),  # 产品明细

    url(r'^logout', views.logout, name='logout'),  # 登录初始化页面
    url(r'^web/login$', views.web_login, name='web/login'), #登录初始化页面
    url(r'^web/loding/login$', views.login, name='web/loding/login'),#登录检查
    url(r'^web/regist', views.regist, name='regist'),#注册初始化页面
    url(r'^web/create', views.regist_create, name='create'),#注册数据创建

    # url(r'^typography', typography.typography, name='typography'),  # 登录初始化页面



]
