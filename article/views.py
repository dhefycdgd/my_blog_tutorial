from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
'''
def home(request):
  return HttpResponse("(home)Hello World,django!!!")
'''
  
def detail(request):
  return HttpResponse("(detail)You're looking at my_args") 
 
def test(request):
  return render(request, 'test.html',{'current_time': datetime.now()})
  
def home(request):
  post_list = Article.objects.all() #获取全部的Article对象
  return render(request, 'home.html', {'post_list' : post_list})
 
 
 
 
