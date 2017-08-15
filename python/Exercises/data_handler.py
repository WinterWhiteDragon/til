# 반 성적을 가져와서 연관된 모든 연산을 할 수 있어야 하며
	# 연산한 결과를 caching해야하고 등등등
# NormDist class를 상속 받을 것인가 합성할 것인가? Inheritance or Composition
	# class DataHandler(NormDist):로 상속,
	# OR mem = NormDist()라는 class member로 합성,
	# OR self.member = NormDist()라는 instance member로 합성
		## DataHandler는 NormDist와 is-a 관계가 아니다... 그러면 합성 사용 결정?
		## 객체별로 가질 필요 없이 class method로 잡아놓으면 된다

from openpyxl import *
from normal_dist import *
	# import openpyxl을 하면, import한 function을 쓸 때마다 openpyxl.<function명>을 써야한다

class DataHandler:
	evaluator = NormDist()

	@classmethod
	def get_data_from_excel(cls, filename):
		# 이것이 class method이어야하는 이유:
			# instance method는 객체를 만든 후 호출한다.
			# __init__에서 객체를 만드는데, 만들려면 이 method의 출력값이 필요하다.
			# 만약 이 method가 instance method이면 paradox에 빠진다.
				# instance method를 실행하려면 init이 작동해야하는데, init을 실행하려면 instance method가 작동해야한다...
		wb = load_workbook(filename)
		g = (wb.active).rows
		dic = {}
		for name, score in g:
			dic.update({name.value : score.value})
		return dic


	def __init__(self, filename, classname):
		self.rawdata = DataHandler.get_data_from_excel(filename)
			# excel에서 데이터를 받아서 {'이름': XX, '점수': XX} 형태로 저장
		self.classname = classname
		self.cache = {}
			# 가져온 데이터랑 필요할 때마다 연산된 결과값을 저장해두는 역할

	# 요소 A가 B에 들어있나? ==> if A in B: ==> 들어있으면 true, 안 들어있으면 false

	def get_cache(self):
		return self.cache

	def get_rawdata(self):
		return self.rawdata

	def get_scores(self):
		if 'scores' not in self.cache:
			self.cache['scores'] = list(self.rawdata.values())
		return self.cache['scores']
	# 캐시 이용법
		# cache에 'scores' key에 해당하는 value가 있는지 확인한다
		# 없다면 새로이 연산을 하여 'scores' key와 values를 cache에 저장한다
		# 있다면 'scores' key로 찾아서 반환만 할 뿐이다

	def get_average(self):
		if 'average' not in self.cache:
			avrg = self.evaluator.average(self.get_scores())
			self.cache['average'] = avrg
			# self.evaluator.average(self.cache['scores'])라고 하면 안된다.
				# 혹시 get_scores()를 아직 호출하지 않았을 경우 에러난다.
			# 아직 get_scores()를 호출하지 않았다면, get_average를 호출하면서 get_scores()도 호출된다.
		return self.cache['average']
			# key가 없어서 에러날 우려가 있다면 .get()을 사용하면 되지만,
				# 여기서는 key가 없을 시 if문이 실행되니까 에러나지 않는다

	def get_variance(self):
		if 'variance' not in self.cache:
			var = self.evaluator.variance(self.get_scores(), self.get_average())
			self.cache['variance'] = var
		return self.cache['variance']

	def get_stn_dev(self):
		if 'stn_dev' not in self.cache:
			stndev = self.evaluator.stn_dev(self.get_variance())
			self.cache['stn_dev'] = stndev
		return self.cache['stn_dev']

	def who_is_highest(self):
		if 'highest' not in self.cache:
			self.cache['highest'] = reduce(lambda a, b: a if self.rawdata.get(a) > self.rawdata.get(b) else b, self.rawdata.keys())
			# self.cache['highest'] = reduce(lambda a, b: a if a>b else b, self.get_scores())는 안된다
				# value로 비교를 하지만, 필요한 것은 가장 높은 점수를 가진 key이기 때문이다
		return self.cache['highest']

	def get_highest(self):
		return self.rawdata[self.who_is_highest()]
	
	def who_is_lowest(self):
		if 'lowest' not in self.cache:
			self.cache['lowest'] = reduce(lambda a, b: b if self.rawdata.get(a) > self.rawdata.get(b) else a, self.rawdata.keys())
		return self.cache['lowest']

	def WhoIsLowest(self):
		return self.rawdata[self.who_is_lowest]

	def GetLowestScore(self):
		pass

	# From)) GitHub CSS_3rd => OOP => data_analysis => datahandler.py
	def GetEvaluation(self, total_avrg):
		print('*' * 75 + '\n')
		print(" :: %s 반 성적 분석 결과 :: " % self.classname + '\n')
		print(
        "{0}반의 평균은 {1}점이고 분산은 {2}이며, 따라서 표준편차는{3}이다.".format(
            self.classname,
            self.get_average(),
            self.get_variance(),
            self.get_stn_dev()) + '\n')
		print('*' * 75 + '\n')
		print(" :: %s 반 종합 평가 :: " % self.classname + '\n')
		print('*' * 75 + '\n')
		self.evaluateClass(total_avrg)

	def evaluateClass(self, total_avrg):
		avrg = self.get_average()
		std_dev = self.get_stn_dev()

		if avrg <total_avrg and std_dev >20:
			print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다." + '\n')
		elif avrg > total_avrg and std_dev >20:
			print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!!" + '\n')
		elif avrg < total_avrg and std_dev <20:
			print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!!" + '\n')
		elif avrg > total_avrg and std_dev <20:
			print("성적도 평균 이상이고 학생들의 실력차도 크지 않다." + '\n')

if __name__ == "__main__":
	dh = DataHandler('class_1.xlsx', '3-3')
	print(dh.who_is_highest())
	print(dh.who_is_lowest())
	print(dh.get_average())
	print(dh.get_cache())
	print(dh.get_rawdata())
