import requests
from bs4 import BeautifulSoup
from getpass import getpass
import pandas as pd



def login_check(user_id, user_pwd):

    session = requests.session()

    URL = 'https://kutis.kyonggi.ac.kr/webkutis/view/hs/wslogin/loginCheck.jsp'
    user_id = user_id
    user_pwd = getpass(user_pwd)

    data = {
        'username': '',
        'password': '',
        'id': user_id,
        'pw': user_pwd,
        'idChk2': 'on'
    }

    response = session.post(URL, data=data)
    response.raise_for_status()

    text = response.text
    if text.find('alert') == -1:
        return True
    else:
        if text.find('flag=0') != -1:
            return True


    session.close()


def get_html(url):
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

