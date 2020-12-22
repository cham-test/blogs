from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from blog.models import Blog, Post
from .models import Subscription, ReadPost

from .forms import AddPostForm
# Create your views here.


class AccountView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(blog__user=request.user)
        return render(request, 'user/account.html', {'posts': posts})


class CreatePostView(CreateView, LoginRequiredMixin):
    form_class = AddPostForm
    template_name = 'user/add_post.html'
    success_url = reverse_lazy('user:account')

    def form_valid(self, form):
        blog = Blog.objects.get(user=self.request.user)
        form.instance.blog = blog
        return super().form_valid(form)