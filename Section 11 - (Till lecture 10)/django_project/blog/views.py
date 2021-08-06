from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView, CreateView


class HomeListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    extra_context = {'title': 'Home Django project'}
    ordering = ["-post_created"]
    template_name = 'blog/homepage.html'


class PostDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AboutTemplateView(TemplateView):
    extra_context = {'title': 'About Django project'}
    template_name = 'blog/about.html'
