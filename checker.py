'''
maj_dict = {
    전공: [0.줄임말, 1.단일전공학점, 2.단일전공전필, 3.단일전공선필, 4.복수전공학점, 5.복수전공전필, 6.복수전공선필, 7.총이수학점]
    }
'''
maj_dict = {
    '경영정보전공': ['경정', 60, 7, 0, 45, 4, 0, 130],
    '회계세무전공': ['회세', 60, 9, 0, 45, 4, 0, 130],
    '경영학과': ['경영', 60, 9, 0, 45, 4, 0, 130]
    }


# 2012 교육과정 (12, 13, 14, 15 학번)
def course_2012(major_1, major_2, foreigner, records):
    global maj_dict
    '''
    0. cul: 교양(기타) 학점
    1. maj_1: 주전공 학점
    2. maj_r1: 주전공 전공필수
    3. maj_c1: 주전공 선택필수
    4. maj_2: 복수전공 학점
    5. maj_r2: 복수전공 전공필수
    6. maj_c2: 복수전공 선택필수
    7. total: 총 학점
    8. necessary: 필수교양 이수여부
    '''
    cul, maj_1, maj_r1, maj_c1, maj_2, maj_r2, maj_c2, total, necessary = 0, 0, 0, 0, 0, 0, 0, 0, False

    # 단일전공 재학생 (외국인 포함)
    if major_2 == False: 
        for div, rec in records.items(): # 각 이수구분
            for sbj in rec: # 각 과목
                if sbj['유효구분'] != '유효':
                    continue
                if '전공필수' in div:
                    maj_r1 += 1
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                elif '선택필수' in rec:
                    maj_c1 += 1
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                elif sbj['이수구분'] == maj_dict[major_1][0]:
                    maj_1 += int(sbj['학점'])
                    total += int(sbj['학점'])
                else:
                    if sbj['교과목명'] in ['글쓰기', '사고와표현']:
                        necessary = True
                    cul += int(sbj['학점'])
                    total += int(sbj['학점'])
        
        maj_1 = maj_dict[major_1][1] - maj_1
        maj_r1 = maj_dict[major_1][2] - maj_r1
        maj_c1 = maj_dict[major_1][3] - maj_c1
        total = maj_dict[major_1][7] - total
        
        return [cul, maj_1, maj_r1, maj_c1, maj_2, maj_r2, maj_c2, total, necessary]


def check(user_id, major_1, major_2, foreigner, records):
    global maj_dict
    result = {}

    if user_id[2:4] in ['12', '13', '14', '15']:
        data = course_2012(major_1, major_2, foreigner, records)
    
    # 단일전공 진단
    if major_2 == False:
        if data[-1] == False:
            result['교양필수'] = '미이수'
        if data[1] > 0:
            result['전공학점'] = data[1]
        if data[2] > 0:
            result['본전공필수'] = data[2]
        if data[3] > 0:
            result['본전공선택'] = data[3]
        if data[7] > 0:
            result['총학점'] = data[7]
        return result