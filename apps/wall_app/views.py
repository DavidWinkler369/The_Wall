from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, UserManager

def index(request):
    print('*'*100)
    print('this is the index route...')
    return render(request, 'wall_app/index.html')

def wall(request):
    print('*'*100)
    print('in the wall...')
    return render(request, 'wall_app/wall.html')
