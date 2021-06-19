from . import views
from django.urls import path

urlpatterns = [
    path('admin/news/post/add/',views.add_new_post, name='add_new_post'),
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('targets/', views.Targets, name='targets'),
    path('summer-club/', views.Club, name='club'),
    path('contact/', views.Contact, name='contact'),
    path('news/detail/<int:post_id>', views.detail, name='detail'),
    path('news/', views.News, name='news'),
    # path('news/new_post/', views.PostCreateView.as_view(), name='new_post'),
]