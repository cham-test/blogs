from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog, Post
# Create your views here.


class BlogsListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(blog_id=self.kwargs["pk"])
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
