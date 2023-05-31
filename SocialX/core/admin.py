from django.contrib import admin
from .models import Profile, Post, LikePost

# Register your models here.
# user model which store data of the user
admin.site.register(Profile)
# post model which store data of post made by user
admin.site.register(Post)
# LikePost model which store data of post which are liked by specific user
admin.site.register(LikePost)
