from django.contrib import messages, auth
from django.shortcuts import render, redirect
from gestion.views import *


# login function...
def login(request):
    if request.user.is_authenticated:
        return redirect('interventions')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, "Yu're now logged in")
            return redirect('interventions')
        else:
            messages.error(request, "Incorrect username ou mot de passe")
            return render(request, 'pages/login.html')

    else:
        return render(request, 'pages/login.html')


# register function...
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#         if password == password2:
#             if User.objects.filter(username=username):
#                 messages.error(request, "username already used")
#                 return render(request, 'pages/register.html')
#             else:
#                 if User.objects.filter(email=email):
#                     messages.error(request, "Email used")
#                     return render(request, 'pages/register.html')
#                 else:
#                     user = User.objects.create_user(username=username, email=email, password=password,
#                                                     first_name=first_name, last_name=last_name)
#                     user.save()
#                     messages.success(request, "You are now register and you can login")
#                     return render(request, 'pages/login.html')
#
#         else:
#             messages.error(request, "Passwords dont match")
#             return render(request, 'pages/register.html')
#     else:
#         return render(request, 'pages/register.html')


# logout function...
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return

