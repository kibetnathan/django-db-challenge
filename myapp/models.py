from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.email

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your name:'
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your email:'
            }
        )
    )
    subject = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject:'
            }
        )
    )
    message = forms.TextField(
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Give your report:'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Custom validation
        if 'example.com' in email:
            raise forms.ValidationError('Example.com emails are not allowed \:\\')
        return email

