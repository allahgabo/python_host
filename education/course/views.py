from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



def index(requset):
	return render(requset,'course/index.html',{})


class HomeView(ListView):
	model=Post
	template_name='course/home.html'