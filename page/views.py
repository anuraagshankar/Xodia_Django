from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError
from .models import *


class Index(View):
    def get(self, request):
        return render(request, 'page/index.html')


class Signup(View):
    def get(self, request):
        return render(request, 'page/signup.html')


class Login(View):
    def get(self, request):
        return render(request, 'page/login.html')


class CreatePlayer(View):

    def post(self, request):
        try:
            u = User.objects.create_user(request.POST["username"], "", request.POST["password"])
            u.save()
            p = Player(user=u, mobileNumber=request.POST["mobileNo"], college=request.POST["college"])
            p.gamesWon = request.POST["gamesWon"]
            p.gamesLost = request.POST["gamesLost"]
            p.gamesDrawn = request.POST["gamesDrawn"]
            p.points = request.POST["points"]
            p.save()
        except IntegrityError:
            username = request.POST["username"]
            return render(request, 'page/user_exists.html', {'username': username})
        else:
            return render(request, 'page/index.html')


class CheckPlayer(View):
    def get(self, request):
        if request.user.is_authenticated:
            player = Player.objects.get(user=request.user)
            return render(request, 'page/show_details.html', {'player': player})

    def post(self, request):
        un = request.POST["username"]
        pw = request.POST["password"]

        u = authenticate(username=un, password=pw)

        if u is not None:
            login(request, u)
            player = Player.objects.get(user=u)
            return render(request, 'page/show_details.html', {'player': player})
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return render(request, 'page/login.html')
