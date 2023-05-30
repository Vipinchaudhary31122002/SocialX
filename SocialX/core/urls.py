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
    path('upload', views.upload, name='upload')
]
