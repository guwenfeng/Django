 # -*- coding: utf-8 -*-
from django.db import  models
from django.db import models
import django.utils.timezone as timezone


class Product_Product(models.Model):
    name = models.CharField('名称', max_length=20)
    price = models.DecimalField('单价', max_digits=210, decimal_places=2)
    cost = models.DecimalField('成本', max_digits=16, decimal_places=2)
    code = models.CharField('条码', max_length=13)
    # img = models.ImageField('图片', upload_to='./sale/static/photos', blank=True)
    # img_name = models.CharField('图片名称',max_length=20)
    add_date = models.DateTimeField('创建日期', auto_now_add =True)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)



class Res_Partner(models.Model):
    name = models.CharField('名称', max_length=13)
    addres = models.CharField('地址', max_length=13)
    phone = models.CharField('电话', max_length=13)
    add_date = models.DateTimeField('创建日期', auto_now_add =True)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)

class Sale_Order(models.Model):
    number = models.CharField('单号', max_length=13)
    date = models.DateField('日期', max_length=13)
    partner_id = models.ForeignKey(Res_Partner, "业务伙伴")
    add_date = models.DateTimeField('创建日期', auto_now_add =True)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)

class Order_line(models.Model):
    product_id = models.ForeignKey(Product_Product, '产品')
    uom = models.CharField('单位', max_length=5)
    qry = models.DecimalField('数量', max_digits=10, decimal_places=2)
    price = models.DecimalField('单价', max_digits=10, decimal_places=2)
    amount = models.DecimalField('金额', max_digits=16, decimal_places=2)
    sale_id = models.ForeignKey(Sale_Order, '主表')
