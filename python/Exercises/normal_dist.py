# 정규 분포 관련 함수용 library
	# 내용: 평균, 분산, 정규분포의 함수 3개

import math
from functools import reduce


class NormDist:
	# __init__을 만들지 않느다면 default construct가 생성된다.
		# 여기서는 멤버 없이 함수만 모아놓은 것이기에 만들 필요가 없다.
	def average(self, scores):
		average = reduce(lambda a, b: a + b, scores) / len(scores)
		return average

	def variance(self, scores, avrg):
		variance = round(reduce(lambda a, b: a + b, map(lambda s: (s - avrg)**2, scores)) / len(scores), 2)
		return variance

	def stn_dev(self, var):
		stn_dev = round(math.sqrt(var), 2)
		return stn_dev

# 이렇게 다 했으면 test code 돌려봐야한다
if __name__ == "__main__":
	li = [1, 2, 3, 4, 5]
	nd = NormDist()
	av = nd.average(li)
	var = nd.variance(li, av)
	stn_dev = nd.stn_dev(var)
	print(av)
	print(var)
	print(stn_dev)