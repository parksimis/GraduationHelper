from mdict import dict_select 

# 2012/2016 교육과정 (12, 13, 14, 15, 16 학번)
def course_2012(major_1, major_2, foreigner, records, maj_dict):
    '''
    0. cul: 교양(기타) 학점
    1. maj_1: 본전공 학점
    2. maj_r1: 본전공 전공필수
    3. maj_c1: 본전공 선택필수
    4. maj_2: 복수전공 학점
    5. maj_r2: 복수전공 전공필수
    6. maj_c2: 복수전공 선택필수
    7. total: 총 학점
    8. necessary: 필수교양 이수여부
    '''
    cul, maj_1, maj_r1, maj_c1, maj_2, maj_r2, maj_c2, total, necessary = 0, 0, 0, 0, 0, 0, 0, 0, False

    for div, rec in records.items(): # 각 이수구분
        for sbj in rec: # 각 과목
            if sbj['유효구분'] != '유효':
                continue
            if '전공필수' in div:
                if div[5:-1] in major_1: # 본전공
                    maj_r1 += 1
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                elif major_2 != False and div[5:-1] in major_2: # 복수전공
                    maj_r2 += 1
                    maj_2 += int(sbj['학점'])
                    tatal += int(sbj['학점'])
                else: # 기타
                    cul += int(sbj['학점'])
                    total += int(sbj['학점'])
            elif '선택필수' in rec:
                if div[5:-1] in major_1: # 본전공
                    if '중어중문' in major_1:
                        maj_r1 += 1
                    else:
                        maj_c1 += 1
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                elif major_2 != False and div[5:-1] in major_2: # 복수전공
                    maj_c2 += 1
                    maj_2 += int(sbj['학점'])
                    tatal += int(sbj['학점'])
                else: # 기타
                    cul += int(sbj['학점'])
                    total += int(sbj['학점'])
            elif sbj['이수구분'] == maj_dict[major_1][0]:
                maj_1 += int(sbj['학점'])
                total += int(sbj['학점'])
            elif major_2 != False and sbj['이수구분'] == maj_dict[major_2][0]:
                maj_2 += int(sbj['학점'])
                total += int(sbj['학점'])
            else:
                if sbj['교과목명'] in ['글쓰기', '사고와표현']:
                    necessary = True
                cul += int(sbj['학점'])
                total += int(sbj['학점'])
    
    if major_2 == False:
        maj_1 = maj_dict[major_1][1] - maj_1
        maj_r1 = maj_dict[major_1][2] - maj_r1
        maj_c1 = maj_dict[major_1][3] - maj_c1
    else:
        maj_1 = maj_dict[major_1][4] - maj_1
        maj_r1 = maj_dict[major_1][2] - maj_r1
        maj_c1 = maj_dict[major_1][3] - maj_c1
        maj_r2 = maj_dict[major_2][5] - maj_r2
        maj_c2 = maj_dict[major_2][6] - maj_c2
    if foreigner == True:
        cul = 15 - cul
    else:
        cul = 35 - cul
    total = maj_dict[major_1][7] - total
    
    return [cul, maj_1, maj_r1, maj_c1, maj_2, maj_r2, maj_c2, total, necessary]


# 2017 교육과정 (17 학번)
def course_2017(major_1, major_2, foreigner, records, maj_dict):
    '''
    0. cul: 교양(기타) 학점
    1. maj_1: 본전공 학점
    2. maj_r1: 본전공 전공필수
    3. maj_c1: 본전공 선택필수
    4. maj_2: 복수전공 학점
    5. maj_r2: 복수전공 전공필수
    6. maj_c2: 복수전공 선택필수
    7. total: 총 학점
    8. necessary: 필수교양 학점
    '''
    cul, maj_1, maj_r1, maj_c1, maj_2, maj_r2, maj_c2, total, necessary = 0, 0, 0, 0, 0, 0, 0, 0, 0

    for div, rec in records.items(): # 각 이수구분
        for sbj in rec: # 각 과목
            if sbj['유효구분'] != '유효':
                continue
            if '전공필수' in div:
                if div[5:-1] in major_1: # 본전공
                    maj_r1 += 1
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                elif major_2 != False and div[5:-1] in major_2: # 복수전공
                    maj_r2 += 1
                    maj_2 += int(sbj['학점'])
                    tatal += int(sbj['학점'])
                else: # 기타
                    cul += int(sbj['학점'])
                    total += int(sbj['학점'])
            elif '선택필수' in rec:
                if div[5:-1] in major_1: # 본전공
                    maj_c1 += 1
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                elif major_2 != False and div[5:-1] in major_2: # 복수전공
                    maj_c2 += 1
                    maj_2 += int(sbj['학점'])
                    tatal += int(sbj['학점'])
                else: # 기타
                    cul += int(sbj['학점'])
                    total += int(sbj['학점'])
            elif sbj['이수구분'] == maj_dict[major_1][0]:
                maj_1 += int(sbj['학점'])
                total += int(sbj['학점'])
            elif major_2 != False and sbj['이수구분'] == maj_dict[major_2][0]:
                maj_2 += int(sbj['학점'])
                total += int(sbj['학점'])
            else:
                if sbj['교과목명'] in ['진리탐구', '공감소통', '사랑실천']:
                    necessary += int(sbj['학점'])
                cul += int(sbj['학점'])
                total += int(sbj['학점'])
    
    if major_2 == False:
        maj_1 = maj_dict[major_1][1] - maj_1
        maj_r1 = maj_dict[major_1][2] - maj_r1
        maj_c1 = maj_dict[major_1][3] - maj_c1
    else:
        maj_1 = maj_dict[major_1][4] - maj_1
        maj_r1 = maj_dict[major_1][2] - maj_r1
        maj_c1 = maj_dict[major_1][3] - maj_c1
        maj_r2 = maj_dict[major_2][5] - maj_r2
        maj_c2 = maj_dict[major_2][6] - maj_c2
    if foreigner == True:
        cul = 18 - cul
        necessary = True
    else:
        if necessary >= 4:
            necessary = True
        else:
            necessary = False
        cul = 35 - cul
    total = maj_dict[major_1][7] - total
    
    return [cul, maj_1, maj_r1, maj_c1, maj_2, maj_r2, maj_c2, total, necessary]


# main function
def check(user_id, major_1, major_2, foreigner, records):
    maj_dict = dict_select(user_id[2:4])
    result = {}

    if user_id[2:4] in ['12', '13', '14', '15', '16']:
        data = course_2012(major_1, major_2, foreigner, records, maj_dict)
    if user_id[2:4] == '17':
        data = course_2017(major_1, major_2, foreigner, records, maj_dict)

    if data[8] == False:
        result['필수교양'] = '미이수'
    if data[0] > 0:
        result['교양학점'] = data[0]
    if data[1] > 0:
        result['본전공학점'] = data[1]
    if data[2] > 0:
        result['본전공필수'] = data[2]
    if data[3] > 0:
        result['본전공선택'] = data[3]
    if data[4] > 0:
        result['복수전공학점'] = data[4]
    if data[5] > 0:
        result['복수전공필수'] = data[5]
    if data[6] > 0:
        result['복수전공선택'] = data[6]
    if data[7] > 0:
        result['총학점'] = data[7]

    return result