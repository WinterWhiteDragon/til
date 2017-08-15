from openpyxl import *
from _2nd_library import *

raw_data = get_rawdata_from_excel('class_1.xlsx')
scores = list(raw_data.values())
avrg = average(scores)
var = variance(scores, avrg)
standard_deviation = stn_dev(var)
print("Average : {}, Variance : {}, Standard Deviation : {}".format(avrg, var, standard_deviation))
