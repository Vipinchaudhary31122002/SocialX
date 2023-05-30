from .models import Profile, Post
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# view for the homepage
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile, 'posts':posts})

# view for signup page
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is Taken by other user')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is Taken by other user')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()

                # Log user in and redirect to setting page
                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request, user_login)

                # create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
            messages.info(request, 'Password not Match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
        
# view for signin page
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
        
# view when the user clicks on the logout button in the homepage
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

# view for the settings page
@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    # after taking input from the user saving the changed data in the database
    if request.method == 'POST':
        # if the user has upload profile images
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        # when the user have not upload the profile images
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('settings')
    return render(request, 'setting.html', {'user_profile': user_profile})

# view for upload post
@login_required(login_url='signin')
def upload(request):
    # storing the post made by user
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')





