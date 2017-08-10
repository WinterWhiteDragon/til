# 함수 인터페이스 = signature
    # <함수명>(<인자목록>)을 입력하면 <반환값>을 사용자에게 반환해 주는 것을 interface라고 한다
# interface와 구현부(implementation)를 나누는 것이 "추상화"
    # 추상화를 한다면 interface만 필요하고 구현부를 알 필요가 없다

# interface 만들기 예시
'''
	This is the library for "Procedural Programming (2017.08.07)"
'''
import math
from openpyxl import *
from functools import reduce

def get_rawdata_from_excel(filename):
    '''
    '(apostrophe) 3개를 앞 줄에 놓고 또 3개를 마지막 줄에 놓으면 사이에 있는 것들은 주석처리로 설명문을 적을 수 있다 
    '''     
    wb = load_workbook('class_1.xlsx')
    ws = wb.active
    raw_data = {}
    gener = ws.rows
    for c1, c2 in gener:
        raw_data.update({c1.value : c2.value})
    return raw_data
    # 이제 from _1st_library import *하면 이 파일의 함수를 import하여 사용할 수 있다

def get_scores_from_excel(filename):
    scores = []
    raw_data = get_rawdata_from_excel(filename)
    for score in raw_data.values():
        scores.append(score)
    return scores

def get_avrg_from_scores(filename):
    scores = get_scores_from_excel(filename)
    avrg = reduce(lambda a, b: a + b,  scores)/len(scores)
    return avrg

def get_variance_from_scores(filename):
    scores = get_scores_from_excel(filename)
    avrg = get_avrg_from_scores(filename)
    variance = round(reduce(lambda a, b: a + b, map(lambda x: (x - avrg)**2, scores))/len(scores), 1)
    return variance

def stn_dev(filename):
    variance = get_variance_from_scores(filename)
    stn_dev = round(math.sqrt(variance), 1)
    return stn_dev

def evaluateClass(avrg, total_avrg, std_dev, sd):
    '''
    evaluateClass(avrg, total_avrg, std_dev, sd) -> None
    avrg : 반 성적 평균
    total_avrg : 학년 전체 성적 평균
    std_dev : 반의 표준 편차
    sd : 원하는 표준 편차 기준
    '''
    if avrg <total_avrg and std_dev >sd:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > total_avrg and std_dev >sd:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < total_avrg and std_dev <sd:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > total_avrg and std_dev <sd:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

# if __name__ == "__main__":
    # 만약 이것이 들어가있는 파일을 메인 실행 파일로 실행하면 if 문 하위 실행문들을 실행한다
    # 하지만 이것이 들어가있는 파일을 module로 import하는 경우에는 if 문 하위 실행문들을 실행하지 않는다
    # 이것은 주로 파일이 library일 때 테스트 코드로 사용한다.
