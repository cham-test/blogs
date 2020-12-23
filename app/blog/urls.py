from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('list/', views.BlogsListView.as_view(), name='list'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('read-post/<int:pk>', views.ReadPostView.as_view(), name='read-post')
]