from django.http.response import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Blog, Post
from user.models import Subscription, ReadPost
# Create your views here.


class BlogsListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscriptions'] = Blog.objects.filter(subscription_blog__user=self.request.user)
        return context


class ReadPostMixin:
    def get_read_post(self) -> ReadPost:
        return Post.objects.filter(read_post_post__user=self.request.user)

    def create_read_post(self) -> ReadPost:
        read_post = ReadPost.objects.create(user=self.request.user,
                                            post_id=self.kwargs['pk'])
        read_post.save()
        return read_post

    def delete_read_post(self) -> tuple:
        read_post = ReadPost.objects.get(user=self.request.user,
                                         post=self.kwargs['pk'])
        return read_post.delete()


class BlogDetailView(DetailView, ReadPostMixin):
    model = Blog
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(blog_id=self.kwargs["pk"])
        context['read_posts'] = self.get_read_post()
        return context


class PostDetailView(DetailView, ReadPostMixin):
    model = Post
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        try:
            ReadPost.objects.get(user=self.request.user,
                                 post_id=self.kwargs['pk'])
        except ObjectDoesNotExist:
            self.create_read_post()
        return super().get(request, *args, **kwargs)


class ReadPostView(View, ReadPostMixin):
    def post(self):
        self.create_read_post()
        return JsonResponse({"success": True}, status=200)

    def delete(self):
        self.delete_read_post()
        return JsonResponse({"success": True}, status=200)
