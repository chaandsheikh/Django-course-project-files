from django.shortcuts import render
from . models import Blog

def homepage(request):
    blogs = Blog.objects.all()
    content = {'title': 'Home Django project',
               'blogs': blogs}
    return render(request, 'blog/homepage.html', content)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Django project'})
