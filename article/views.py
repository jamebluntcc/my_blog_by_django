#encoding='utf-8'
import sys
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.
reload(sys)
sys.setdefaultencoding('utf-8')

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = {title},category = {category},date_time = {date_time},content = {content}".format(title=post.title,
                                                                                                      category=post.category,
                                                                                                      date_time=post.date_time,
                                                                                                      content=post.content))

    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})


