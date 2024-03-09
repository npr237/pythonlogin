from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            # No backend authenticated the credentials
            # Return an error message or handle the failed login attempt
            return render(request, 'login.html')
   
    
    return render(request,'login.html')
def logoutuser(request):
    # Log out the user
    logout(request)
    # Redirect to a logout success page or any other page you desire
    return redirect('/login')
    return render(request,'logout.html')        