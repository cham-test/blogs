from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('account/', views.AccountView.as_view(), name='account'),
    path('add_post/', views.CreatePostView.as_view(), name='add_post'),
    path('subscribe/', views.SubscribingView.as_view(), name='subscribe'),
]