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
    scrapping -> True 시 html tag scrapping(default=True)
    output : html -> 해당 주소의 html 페이지
    '''
    response = session.get(url)
    response.raise_for_status()

    html = BeautifulSoup(response.text, "html.parser")
    return html


def get_user_info(session):
    html = get_html('https://kutis.kyonggi.ac.kr:443/webkutis/view/hs/wshj1/wshj111s.jsp?submenu=1&m_menu=wsco1s02&s_menu=wshj111s', session)

    department = get_user_department(html)
    foreigner = check_foreigner(html)
    return department, foreigner



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
