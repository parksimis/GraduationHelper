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
        double_major = engine.check_double_major(session)
        context = {
            'department': department,
            'foreigner': foreigner,
            'double_major': double_major,
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

    table = engine.crawl_table(session)
    registration = engine.crawl_registration(session)

    context = {
        'table': table,
    }

    return render(request, 'main/result.html', context)


