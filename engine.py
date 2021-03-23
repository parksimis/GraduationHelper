import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def login(user_id, user_pwd):
    session = requests.session()

    URL = 'https://kutis.kyonggi.ac.kr/webkutis/view/hs/wslogin/loginCheck.jsp'

    data = {
        'username': '',
        'password': '',
        'id': user_id,
        'pw': user_pwd,
        'idChk2': 'on'
    }

    response = session.post(URL, data=data)
    response.raise_for_status()
    return response, session

def login_check(response, session):

    text = response.text
    if text.find('alert') == -1 or text.find('flag=0') != -1:
        return True, session
    else:
        return False

def get_html(url, session):
    '''
    URL 주소를 받아서, html 페이지를 scrapping 하는 method
    ========================================================
    input :
    url -> 원하는 페이지 url 주소
    session -> 유지되는 session
    output : html -> 해당 주소의 html 페이지
    '''
    response = session.get(url)
    response.raise_for_status()

    html = BeautifulSoup(response.text, "html.parser")
    return html

def get_user_department(html):

    department = html.select('thead')[1].select('td')[6].text
    if department.find('전공') != -1:
        department = department.split('전공')[0] + '전공'
    elif department.find('학과') != -1:
        department = department.split('학과')[0] + '학과'
    else :
        department = department.split('학부')[0] + '학부'

    return department

def check_foreigner(html):
    foreigner = html.select('thead')[1].select('td')[16].text
    if foreigner == '외국인':
        return True
    else:
        return False

def check_double_major(session):
    html = get_html('https://kutis.kyonggi.ac.kr/webkutis/view/hs/wshj1/wshj115s.jsp?submenu=2', session)

    tbody = html.select('.list06 tbody tr')
    double_major = None
    for i in range(len(tbody)):
        tr = tbody[i].select('td')
        if (tr[2].text == '제2전공' and tr[4].text == '전공승인'):
            double_major = tr[3].text

    return double_major

def get_user_info(session):
    html = get_html('https://kutis.kyonggi.ac.kr:443/webkutis/view/hs/wshj1/wshj111s.jsp?submenu=1&m_menu=wsco1s02&s_menu=wshj111s', session)

    department = get_user_department(html)
    foreigner = check_foreigner(html)
    return department, foreigner

# def crawl_registration(session):
#     html = get_html('https://kutis.kyonggi.ac.kr/webkutis/view/hs/wssu3/wssu320s.jsp?m_menu=wsco1s05&s_menu=wssu320s', session)
#
#     tbody = html.select('.list06 tbody tr')
#     sugang = []
#     registration = pd.DataFrame(columns=['이수구분', '인증구분', '년도 학기', '학수코드',
#                           '교과목명', '학점', '설계학점', '등급', '유효구분'])
#
#     for i in range(len(tbody)):
#         tr = tbody[i].select('td')
#
#         subject = tr[2].text.replace('보기', '').strip()
#         div = tr[3].text
#         grade = int(tr[4].text)
#
#         sugang.append([div, subject, grade])
#
#     for i in range(len(sugang)):
#         registration.loc[len(registration), ['이수구분', '교과목명', '학점']] = sugang[i]
#
#     registration.fillna('', inplace=True)
#     registration = registration.to_dict('records')
#
#     return registration

def crawl_table(session):
    html = get_html('http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssj1/wssj170s.jsp?submenu=2', session)

    thead = html.select_one('thead')  # 테이블 box 가져오기
    tr = thead.select('tr')  # tr만 뽑아오기

    hakjeom = dict()
    table = []
    temp_df = pd.DataFrame(columns=tr[0].text.strip().split('\n'))

    for i in range(1, len(tr)):
        row = tr[i].text.strip().split('\n')

        if len(row) == 9:  # 총 칼럼이 9개인 것은 정상적인 것이므로 제외
            table.append(row)

        elif len(row) == 7:  # 칼럼이 7개인 경우에는 앞에 두개 넣어줌
            row = [table[-1][0], " "] + row
            table.append(row)

        if len(row) == 2:
            for j in range(len(table)):
                temp_df.loc[j] = table[j]

            div_name = re.sub('[^가-힣()]', '', row[0])
            hakjeom[div_name] = temp_df.to_dict('records')
            temp_df.drop(temp_df.index, inplace=True)
            table = []

    return hakjeom
