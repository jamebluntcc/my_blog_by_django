#encoding='utf-8'
import sys
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Article
# Create your views here.
reload(sys)
sys.setdefaultencoding('utf-8')

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=int(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})


