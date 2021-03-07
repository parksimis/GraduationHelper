from django.shortcuts import render, redirect
from .forms import LoginForm
import engine

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def crawling(request):
    user_id = request.POST.get('user_id')
    user_pwd = request.POST.get('user_pwd')
    print(user_id, user_pwd)

    user_response = engine.login(user_id, user_pwd)
    if engine.login_check(user_response):
        print('OK')
        return render(request, 'main/index.html')
    else:
        return render(request, 'main/login_fail.html')

