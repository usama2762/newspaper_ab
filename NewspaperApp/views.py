from django.shortcuts import render
from django.http import HttpResponse
# import newspaper // i am commenting this line as there is no directory with newspaper name
# from newspaper import Article
import json
# Create your views here.
from .models import *
import datetime


def index(request):
    rs = RequestStore(request_time=datetime.datetime.now(), request_url="/",request_method=request.method)
    rs.save()
    return render(request, 'index.html')


def article(request, value):
    return HttpResponse("your value is " + value)


def detail(request):
    rs = RequestStore(request_time=datetime.datetime.now(), request_url="/articleDetail",request_method=request.method)
    rs.save()
    query = request.GET.get("u")
    #	as there is no model named Article so i am commenting this line
    # article = Article(url=query)
    # article.download()
    # article.parse()
    return render(request, 'post.html', {'article': article})


def dummy_view1(request, random_string):
    rs = RequestStore(request_time=datetime.datetime.now(), request_url="/" + random_string,request_method=request.method,
                      status_code=HttpResponse.status_code)
    rs.save()
    return render(request, 'index.html')
