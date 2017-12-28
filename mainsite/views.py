from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template
# Create your views here.

def homepage(request):
  posts=Post.objects.all()
  template=get_template('index.html')
  now=datetime.now()
  html=template.render(locals()) 
  return HttpResponse(html)

def showpost(request,slug):
	template=get_template('post.html')
	try:
		post=Post.objects.get(slug=slug)
		if post!=None:
			html=template.render({'post':post})
			return HttpResponse(html)
	except:
		return redirect('/')
		