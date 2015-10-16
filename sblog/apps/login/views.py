#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import hashlib,datetime,time

from sblog.models.models.user_models import userInfo

#登陆页面展示
def login(request):
    return render(request,'Account/login.html',context_instance=RequestContext(request))

#登陆过程

def doLogin(request):

    username = request.POST['username'];
    password = request.POST['password'];
    user = userInfo.objects.filter(username=username,password=password);
    if user:
        return HttpResponse(1);
    else:
        return HttpResponse(0);
    #return HttpResponse(username)


def reg(request):
    return render(request,'Account/reg.html')

def doReg():
    return HttpResponse('注册中')
