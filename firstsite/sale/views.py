 # -*- coding: utf-8 -*-
from django.db import  models
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,request
from django.template import RequestContext
from django.contrib.auth.models import User
from . import  models as mod
from django import forms
import json
#表单
class ProductForm(forms.Form):
    name = forms.CharField(label='名称', max_length=20)
    price = forms.DecimalField(label='单价', max_digits=10, decimal_places=2)
    cost = forms.DecimalField(label='成本', max_digits=10, decimal_places=2)
    code = forms.CharField(label='条码', max_length=13)
    img = forms.FileField(label="图片", required=False)

    # class Meta:
    #     model = mod.Product_Product
    #     # fields = '__all__'  # ['name', 'create_at',  ...]


#产品列表
def product_info(request):
    return render(request, 'product_info.html')

#产品列表
def product_data(request):
    products = mod.Product_Product.objects.filter()
    products = mod.Product_Product.objects.all()
    data = []
    for product in products:
        print(product)
        print(product.id)
        lin_data = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'cost': str(product.cost),
            'code': product.code,
            'mod_date': str(product.mod_date),
        }
        data.append(lin_data)
    print (data)
    return HttpResponse(json.dumps({'total':100,'rows':data}), content_type='application/json')



#查询产品信息
def product_eidt(request):
    print (123)
    id=(request.GET['id'])
    if id:
        product=mod.Product_Product.objects.filter(id=id)
    return render(request, 'product_eidt.html',{'product':product[0]})

##
#修改产品信息
def product_eidt_commit(request):
    id=(request.GET['id'])
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        cost = request.POST['cost']
        code = request.POST['code']
        product_data = mod.Product_Product.objects.filter(id=id).update(name= name,price=price,cost=cost,code=code)
        return redirect('/product_info')
    return redirect('/product_info')


#删除产品信息
def product_delete(request):
    id=(request.GET['id'])
    if id:
        product=mod.Product_Product.objects.filter(id=id).delete()
    return redirect('/product_info')

##
#创建产品信息
def product_create(request):
    return render(request, 'product_create.html')


def product_create_commit(request):
    if request.method == 'POST':
        #获得表单数据
        name = request.POST['name']
        price =request.POST ['price']
        cost = request.POST ['cost']
        code = request.POST ['code']
        product_data=mod.Product_Product.objects.create(name= name,price=price,cost=cost,code=code)
        return redirect('/product_info')
    return redirect('/product_info')




