from django.shortcuts import render, redirect
from .forms import LoginForm
import engine

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def crawling(request):
    user_id = request.POST.get('user_id')
    user_pwd = request.POST.get('user_pwd')
    if engine.login_check(user_id, user_pwd):
        print('OK')
    else:
        print('No')
    html = engine.get_html('http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssj1/wssj170s.jsp?submenu=2')

