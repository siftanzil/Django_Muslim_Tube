from django.contrib import admin
from .models import Category, Video, Comment, Like

# Register your models here.
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)
