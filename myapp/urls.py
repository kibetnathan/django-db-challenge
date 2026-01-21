from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('blog/', views.blog_list, name='blog_list'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('contact_us/', views.contact_us, name='contact_us')
]