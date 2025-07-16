from django.db import models
from django.contrib.auth.models import User

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title 
    
# Library model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='librarians')
    
    def __str__(self):
        return self.name


# User roles choices
ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('librarian', 'Librarian'),
    ('member', 'Member'),
]

   
# User profile model to store user roles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    roles = models.CharField(max_length=255, choices=ROLE_CHOICES) 
    
    def __str__(self):
        return f"{self.user.username} - {self.roles}"
