import json

from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, CreateView
from django.http.response import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from blog.models import Blog, Post
from .models import Subscription, ReadPost

from .forms import AddPostForm

from blog.views import ReadPostMixin
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


class SubscribingView(View):
    def post(self, request, *args, **kwargs):
        blog_id = json.loads(request.body).get("blog_id")
        subscription = Subscription.objects.create(user=request.user,
                                                   blog_id=blog_id)
        subscription.save()
        return JsonResponse({"success": True}, status=200)

    def delete(self, request, *args, **kwargs):
        blog_id = json.loads(request.body).get("blog_id")
        subscription = Subscription.objects.get(user=request.user,
                                                blog_id=blog_id)
        subscription.delete()
        return JsonResponse({"success": True}, status=200)


class NewsFeedView(View, ReadPostMixin):
    def _get_subscribed_blog_posts(self) -> Post:
        subscriptions = Subscription.objects.filter(user=self.request.user)
        blogs = []
        for subscription in subscriptions:
            blogs.append(subscription.blog)
        posts = Post.objects.none()
        for blog in blogs:
            posts = posts | Post.objects.filter(blog=blog)
        return posts.order_by('-date_time')

    def get(self, request, *args, **kwargs):
        posts = self._get_subscribed_blog_posts()
        read_posts = self.get_read_post()
        return render(request, 'user/news_feed.html', {'posts': posts,
                                                       'read_posts': read_posts})