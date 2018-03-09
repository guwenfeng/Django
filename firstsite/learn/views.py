#coding=utf-8
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,request
from django.template import RequestContext
from django import forms
from .models import ResUser
from django.db.models import Q


#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(),max_length=16)
    email = forms.EmailField(label='邮箱')
    phone = forms.CharField(label='电话',max_length=13)


def web_login(request):
    return render(request, 'login.html')



#注册
def regist(request):
    return render(request, 'registration.html')

#注册
def regist_create(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            phone = uf.cleaned_data['phone']
            print (username,password)
            #添加到数据库
            ResUser.objects.create(username= username,password=password,email= email,phone=phone)
            return redirect('/web/login')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf}, context_instance=RequestContext(request))




#登陆
def login(request):
    if request.method == 'POST':
        #获取表单用户密码
        data=request.POST
        username = data['username']
        password = data['password']
        print (username,password)
        #获取的表单数据与数据库进行比较
        user =ResUser.objects.get(Q(username__exact = username) | Q(email__exact = username) | Q(phone__exact = username),password__exact = password)
        if user:
            #比较成功，跳转index
            response = HttpResponseRedirect('/index' )
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,3600)
            return response
    return redirect('/web/login')





#退出
def logout(request):
    response = HttpResponseRedirect('/web/login')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response