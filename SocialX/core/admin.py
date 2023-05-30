from django.contrib import admin
from .models import Profile, Post

# Register your models here.
# user model which store data of the user
admin.site.register(Profile)
# post model which store data of post made by user
admin.site.register(Post)
