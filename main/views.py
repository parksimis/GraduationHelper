from django.shortcuts import render, redirect
from .forms import LoginForm
import engine

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def crawling(request):

    user_id = request.POST.get('user_id')
    user_pwd = request.POST.get('user_pwd')

    request.session['user_id'] = user_id
    request.session['user_pwd'] = user_pwd

    user_response, session = engine.login(user_id, user_pwd)

    if engine.login_check(user_response, session):
        department, foreigner = engine.get_user_info(session)
        # request.session['sessions'] = session
        context = {
            'department': department,
            'foreigner': foreigner
        }
        return render(request, 'main/user_detail.html', context)
    else:
        del request.session['user_id']
        del request.session['user_pwd']
        return render(request, 'main/login_fail.html')


def crawl_table(request):
    user_id = request.session['user_id']
    user_pwd = request.session['user_pwd']
    user_response, session = engine.login(user_id, user_pwd)

    tt = engine.crawl_table(session)
    print(tt)

    return render(request, 'main/user_detail.html')


