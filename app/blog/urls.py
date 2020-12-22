from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('list/', views.BlogsListView.as_view(), name='list'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='detail')
]