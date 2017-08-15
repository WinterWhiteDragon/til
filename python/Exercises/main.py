from data_handler import *
# 사용자는 data_handler만 import하면 된다.
	# data_handler 내용(멤버, 메서드 등)이나 data_handler는 무슨 library를 import했는지(normal_dist 등)는 알 필요 없다.

dh = DataHandler('class_1.xlsx', '4-1')

# 평균을 알고싶다면:
# print(dh.get_average())
	# DataHandler class를 전부 연산하는 것이 아니라, 호출한 method 하나만 연산한다.

# 전체 평균을 50으로 가정
dh.GetEvaluation(50)
	# GetEvaluation 메서드 내부에 print명령이 있기 때문에 따로 print()를 쓸 필요가 없다.