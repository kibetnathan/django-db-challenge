from django.urls import path
from . import views
from .views import BlogListCreateAPIView , BlogDetailAPIView, AuthorListAPIView

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('blog/', views.blog_list, name='blog_list'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('contact_us/', views.contact_us, name='contact_us'),

    # api views
    path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('authors/', AuthorListAPIView.as_view(), name='author-list')
]
