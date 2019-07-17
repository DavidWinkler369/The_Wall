from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, UserManager

def index(request):
    print('*'*100)
    print('this is the index route...')
    return render(request, 'wall_app/index.html')

def register(request):
    print('*'*100)
    print('Registering...')
    errors = User.objects.registrationValidation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            firstName = request.POST['fname'],
            lastName = request.POST['lname'],
            email_address = request.POST['email'],
            password = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt())
        )
        request.session['user'] = user.id
        request.session['fname'] = user.first_name
    return redirect('/wall')

def login(request):
    print('*'*100)
    print('logging in...')
    errors = User.objects.loginValidation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.filter(email_address = request.POST['email'])
        request.session['user'] = user[0].id
        request.session['fname'] = user[0].first_name
    return redirect('/wall')


def wall(request):
    print('*'*100)
    print('in the wall...')
    return render(request, 'wall_app/wall.html')
