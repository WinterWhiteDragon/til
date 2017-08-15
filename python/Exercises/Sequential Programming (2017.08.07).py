# Example of how NOT to do procedural programming
    # So I can know how procedural programming works and why it's used

import math
from openpyxl import *
from functools import reduce
    # 연습하기 위해 reduce 사용

    # 1. 파일에서 데이터 읽어와서 자료구조 생성
wb = load_workbook('class_1.xlsx')
ws = wb.active

raw_data = {}
    
gener = ws.rows

for c1, c2 in gener:
    raw_data.update({c1.value : c2.value})

print(raw_data)
    # IDLE에서 실행하려면 F5만 누르면 된다
    # 항상 중간중간에 제대로 실행되는지 시험해볼것

scores = []
for score in raw_data.values():
    scores.append(score)

print(scores)


# reduce를 사용하여 scores의 average구하라
avrg = reduce(lambda a, b: a + b,  scores)/len(scores)
print(avrg)

# variance(분산)을 구라하
    # [(각 학생의 score - avrg) ** 2의 합] / 학생수
    # 학생수는 len(scores)
variance = round(reduce(lambda a, b: a + b, map(lambda x: (x - avrg)**2, scores))/len(scores), 1)
print(variance)

# standard deviation(표준편차)을 구하라
standard_deviation = round(math.sqrt(variance), 1)
print(standard_deviation)

print("평균 : {}, 분산 : {}, 표준편차 : {}".format(avrg, variance, standard_deviation))
