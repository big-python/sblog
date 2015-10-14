#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
def index(request):

    return render(request,'index.html')