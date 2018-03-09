#coding=utf-8

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,request
from django.template import RequestContext
from django import forms
from . import base

def typography(request):

    data=base.base(request)

    return render(request, 'typography.html',{'data':data})

# def typography(request):
#     return redirect('typography.html')