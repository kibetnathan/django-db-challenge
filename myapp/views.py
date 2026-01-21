from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber, Blog
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth import logout

# Create your views here.
def index(request):
    context = {"message" : "Welcome to Django!"}
    return render(request, 'index.html')

def home(request):
    context = {"message" : "Welcome to Django!"}
    return render(request, 'home.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

def contact_us(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # send email
            send_mail(
                f'{subject} from {name}',
                message,
                email,
                ['admin@example.com']
            )
            return render(request, 'contact_success.html')
        
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form' : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been logged out successfully!")
    return redirect('login')

def error_404(request, exception):

    return render(request, '404.html')

