#coding=utf-8

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,request
from django.template import RequestContext
from django import forms
from ..views import ResUser

#登陆成功
def index(request):
    username = request.COOKIES.get('username','')
    if username:
        #查询数据库
        data = base(request)
        return render_to_response('index.html' ,{'data':data})
    else:
        return  redirect( '/web/login')



def base(request):

    user=ResUser.objects.filter(id=1)[0]
    data={
        'username':user.username
    }
    return data



