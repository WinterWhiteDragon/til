# Example of how to do procedural programming

from openpyxl import *
from _1st_library import *

raw_data = get_rawdata_from_excel('class_1.xlsx')
scores = get_scores_from_excel('class_1.xlsx')
avrg = get_avrg_from_scores('class_1.xlsx')
variance = get_variance_from_scores('class_1.xlsx')
standard_deviation = stn_dev('class_1.xlsx')
print("평균 : {}, 분산 : {}, 표준편차 : {}".format(avrg, variance, standard_deviation))

# 모범 답안
# if __name__ == "__main__": 
#     raw_data = get_data_from_excel('class_1.xlsx')
#     scores = list(raw_data.values())
#     avrg = average(scores)
#     variance = variance(scores, avrg)
#     standard_deviation = std_dev(variance)

#     print("평균 :{0}, 분산 : {1}, 표준 편차 : {2}".format(
#         avrg, variance, standard_deviation))
#     evaluateClass(avrg, 50, standard_deviation)