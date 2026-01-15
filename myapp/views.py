from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"message" : "Welcome to Django!"}
    return render(request, 'index.html')