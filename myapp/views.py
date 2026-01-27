from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import Subscriber, Blog, Author
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth import logout
from .serializers import BlogSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.db import IntegrityError

# Create your views here.

# class BlogListCreateAPIView(APIView):
#     def get(self, request):
#         blogs = Blog.objects.select_related('author').all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except IntegrityError:
#                 return Response({'detail' : ' Invalid Data'}, status=status.HTTP_409_CONFLICT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class BlogDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise exceptions.NotFound(f"Blog with ID {pk} not found.")

#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data)
#             except IntegrityError:
#                 return Response({"detail": "Invalid data."}, status=status.HTTP_409_CONFLICT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class AuthorListAPIView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)

# def index(request):
#     context = {"message" : "Welcome to Django!"}
#     return render(request, 'index.html')

# def home(request):
#     context = {"message" : "Welcome to Django!"}
#     return render(request, 'home.html')

# def blog_list(request):
#     blogs = Blog.objects.all()
#     context = {'blogs': blogs}
#     return render(request, 'blog_list.html', context)

# def subscribe(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         if Subscriber.objects.filter(email=email).exists():
#             messages.error(request, 'You are already subscribed.')
#         else:
#             subscriber = Subscriber(email=email)
#             subscriber.save()
#             messages.success(request, 'Thank you for subscribing!')
#             return redirect('subscribe')
#     return render(request, 'subscribe.html')

# def contact_us(request):
#     if request.method == 'POST' :
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
            
#             # send email
#             send_mail(
#                 f'{subject} from {name}',
#                 message,
#                 email,
#                 ['admin@example.com']
#             )
#             return render(request, 'contact_success.html')
        
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form' : form})

# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         messages.info(request, "You have been logged out successfully!")
#     return redirect('login')

# def error_404(request, exception):

#     return render(request, '404.html')

