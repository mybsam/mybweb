from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template
# Create your views here.

def homepage(request):
  template=get_template('index.html')
  html=template.render() 
  return HttpResponse(html)

def passage(request):
	template=get_template('passage.html')
	posts=Post.objects.all()
	html=template.render(locals())
	return HttpResponse(html)
	
		