from django.urls import path
from . import views

urlpatterns = [
    # url of homepage
    path('', views.index, name='index'),
    # url of signup page
    path('signup', views.signup, name='signup'),
    # url of signin page
    path('signin', views.signin, name='signin'),
    # url when user clicks on the logout page
    path('logout', views.logout, name='logout'),
    # url for settings page
    path('settings', views.settings, name='settings'),
    # url for uploading post
    path('upload', views.upload, name='upload'),
    # url when the user like the post
    path('like-post', views.like_post, name='like-post'),
    # url for the profile page of user
    path('profile/<str:pk>', views.profile, name='profile')
]
