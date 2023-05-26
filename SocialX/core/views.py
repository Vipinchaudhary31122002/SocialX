from .models import Profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# view for the homepage
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

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

                # create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')

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