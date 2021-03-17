import requests
from bs4 import BeautifulSoup
from getpass import getpass
import pandas as pd

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

def get_user_info(session):
    html = get_html('https://kutis.kyonggi.ac.kr:443/webkutis/view/hs/wshj1/wshj111s.jsp?submenu=1&m_menu=wsco1s02&s_menu=wshj111s', session)

    department = get_user_department(html)
    foreigner = check_foreigner(html)
    return department, foreigner


def crawl_table(session):
    html = get_html('http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssj1/wssj170s.jsp?submenu=2', session)

    thead = html.select_one('thead')  # 테이블 box 가져오기
    tr = thead.select('tr')  # tr만 뽑아오기

    table = []
    for i in range(len(tr)):
        row = tr[i].text.strip().split('\n')

        if len(row) == 9:  # 총 칼럼이 9개인 것은 정상적인 것이므로 제외
            table.append(row)

        elif len(row) == 7:  # 칼럼이 7개인 경우에는 앞에 두개 넣어줌
            row = [table[-1][0], " "] + row
            table.append(row)
    hakjeom = pd.DataFrame(table[1:], columns=table[0])
    hakjeom = hakjeom[hakjeom['유효구분'] == '유효']

    return hakjeom