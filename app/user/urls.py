from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('account/', views.AccountView.as_view(), name='account'),
    path('add-post/', views.CreatePostView.as_view(), name='add-post'),
    path('update-post/<int:pk>', views.UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<int:pk>', views.DeletePostView.as_view(), name='delete-post'),
    path('subscribe/', views.SubscribingView.as_view(), name='subscribe'),
    path('news-feed/', views.NewsFeedView.as_view(), name='news-feed')
]