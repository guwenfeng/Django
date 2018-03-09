from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^product_data', views.product_data, name='product_data'),  # 获取产品信息
    url(r'^product_info', views.product_info, name='product_info'),  # 获取产品信息
    url(r'^product_create', views.product_create, name='product_create'), #创建页面
    url(r'^procommit', views.product_create_commit, name='procommit'), #提交创建信息
    url(r'^product_eidt/$', views.product_eidt, name='product_eidt'),  # 产品修改页面
    url(r'^pro_commit/$', views.product_eidt_commit, name='pro_commit'),#提交修改信息
    url(r'^product_delete/$', views.product_delete, name='product_delete'),  # 删除产品

]
