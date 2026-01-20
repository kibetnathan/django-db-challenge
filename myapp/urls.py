from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('blog/', views.blog_list, name='blog_list'),
    path('subscribe', views.subscribe, name='subscribe')
]