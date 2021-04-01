import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def login(user_id, user_pwd):
    '''
    사용자 ID와 PW를 받아 로그인해 세션과 response 와 session을 반환하는 함수

    * Parameter
    :param user_id: 사용자 id
    :param user_pwd: 사용자 password

    * Output
    :return:
        response : 로그인한 response 객체
        session : 연결된 session
    '''

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

    return response, session

def login_check(response, session):
    '''
    로그인 후 반환 결과를 해석해 로그인 성패를 확인하는 함수

    * Parameter
    :param response: URL 연결 response
    :param session: URL 연결 세션

    * Output
    :return: 성공여부 : True / False (성공 시 session 같이 반환)
    '''

    text = response.text
    if text.find('alert') == -1 or text.find('flag=0') != -1:
        return True, session
    else:
        return False

def get_html(url, session):
    '''
    URL 주소를 받아서, html 페이지를 scrapping 하는 함수

     * Parameter
    :param url : 원하는 페이지 url 주소
    :param session : 유지되는 session

    * Output
    :return: html : 해당 주소의 html 페이지
    '''

    response = session.get(url)
    response.raise_for_status()

    html = BeautifulSoup(response.text, "html.parser")

    return html


def get_user_department(html):
    '''
    사용자의 학생기본정보 Table 스크래핑해 전공을 가져오는 함수

    * Input
    :param html: get_html에서 넘겨주는 특정 URL의 html 페이지

    * Output
    :return: department : 사용자의 학과
    '''

    department = html.select('thead')[1].select('td')[6].text
    if department.find('전공') != -1:
        department = department.split('전공')[0] + '전공'
    elif department.find('학과') != -1:
        department = department.split('학과')[0] + '학과'
    else:
        department = department.split('학부')[0] + '학부'

    return department


def check_foreigner(html):
    '''
    사용자의 학생기본정보 Table 스크래핑해 외국인을 확인해 결과를 반환하는 함수

    * Input
    :param: html: get_html에서 넘겨주는 특정 URL의 html 페이지

    * Output
    :return: 외국인 여부 : True / False
    '''
    foreigner = html.select('thead')[1].select('td')[16].text
    if foreigner == '외국인':
        return True
    else:
        return False

def get_depart_name(html):
    depart_name = html.select_one('#memInfo dd').text
    depart_name = re.sub('[^가-힣()]', '', depart_name)

    return depart_name

def get_user_info(session):
    '''
    사용자의 기본정보를 스크래핑하는 함수(get_user_department, check_foreigner 종합)

    * Input
    :param session: 연결되는 세션

    * Output
    :return:
        depart_name : 학부(소속)
        department : 사용자 학과
        foreigner : 외국인 여부 (T/F)
    '''
    html = get_html('https://kutis.kyonggi.ac.kr:443/webkutis/view/hs/wshj1/wshj111s.jsp?submenu=1&m_menu=wsco1s02&s_menu=wshj111s', session)

    department = get_user_department(html)
    foreigner = check_foreigner(html)
    depart_name = get_depart_name(html)

    return depart_name, department, foreigner

def check_double_major(session):
    '''
    전공신청 내역 Table을 스크래핑해 제2전공을 확인하는 함수

    * Input
    :param session: 연결되어 있는 세션

    * Output
    :return: double_major : 사용자의 제2전공명(없으면 None)반환
    '''
    html = get_html('https://kutis.kyonggi.ac.kr/webkutis/view/hs/wshj1/wshj115s.jsp?submenu=2', session)

    tbody = html.select('.list06 tbody tr')
    double_major = None
    for i in range(len(tbody)):
        tr = tbody[i].select('td')
        if (tr[2].text == '제2전공' and tr[4].text == '전공승인'):
            double_major = tr[3].text

    return double_major


def crawl_table(session):
    '''
    성적조회 > 이수구분별누적성적 페이지에서 사용자의 학점을 스크래핑 후 처리를 위해 전처리해 반환하는 함수

    * Input
    :param: session: 연결되는 세션

    * Output
    :return: hakjeom : 사용자 학과 테이블(dict)
    '''
    html = get_html('http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssj1/wssj170s.jsp?submenu=2', session)

    thead = html.select_one('thead')  # 테이블 box 가져오기
    tr = thead.select('tr')  # tr만 뽑아오기

    hakjeom = dict()
    table = []
    temp_df = pd.DataFrame(columns=tr[0].text.strip().split('\n'))

    for i in range(1, len(tr)):
        row = tr[i].text.strip().replace('\xa0', '').split('\n')

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