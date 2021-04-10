from django.shortcuts import render, redirect
import engine, checker

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
        depart_name, department, foreigner = engine.get_user_info(session)
        double_major = engine.check_double_major(session)
        context = {
            'depart_name': depart_name,
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

    # 세션에서 저장해놓은 사용자 아이디와 비밀번호 가져오기
    user_id = request.session['user_id']
    user_pwd = request.session['user_pwd']
    # 로그인 재진행
    user_response, session = engine.login(user_id, user_pwd)
    # 사용자 학과
    user_depart = request.POST.get('major')
    # 복수전공 확인 변수 ('True' / 'False' ) 로 들어옴
    double_chk = bool(request.POST.get('double_chk'))
    # 외국인 여부
    foreigner = bool(request.POST.get('foreigner'))
    # 학부 이름
    depart_name = request.POST.get('depart_name')
    depart_name = depart_name.replace('ㆍ', '').replace('▶', '')

    if double_chk is True:
        # 복수전공
        double_major = request.POST.get('double_major')
    else:
        # 단일전공이면 False로 변경
        double_major = False

    table = engine.crawl_table(session)

    result = checker.check(user_id[:4], major_1=user_depart, major_2=double_major, foreigner=foreigner, records=table, depart_name=depart_name)

    grade = ['교양학점', '본전공학점', '복수전공학점', '총학점']

    context = {
        'result': result,
        'grade': grade,
    }

    return render(request, 'main/result.html', context)


