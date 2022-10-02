from django.db import models

from django.contrib.auth.models import AbstractUser

from django.urls import reverse
from django.utils.timezone import now

# Create your models here.


class User(AbstractUser):

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blogs')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " Comment: " + self.content
