from django.db import models
from encrypted_model_fields.fields import EncryptedCharField, EncryptedTextField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    grade_level = models.IntegerField(max_length=2)
    subjects = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    ssn = EncryptedCharField(max_length=20,null=True, blank=True)
    bio = EncryptedTextField()

    def __str__(self):
        return self.username
