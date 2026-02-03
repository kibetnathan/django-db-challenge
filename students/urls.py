from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from . import views
from .views import StudentView, StudentDetailView

# router = DefaultRouter()
# router.register(r'students', views.StudentView)

urlpatterns = [
    # path('', include(router.urls)),
    path('user-profile', views.create_profile, name='create_profile'),
    path('students/', StudentView.as_view(), name='student'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student-list')
]