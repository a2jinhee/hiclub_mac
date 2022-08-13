from django.contrib import admin

from .models import User, Author, Category, Post

# Register your models here.

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
