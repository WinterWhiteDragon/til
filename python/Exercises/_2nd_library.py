'''
	This is the library for "Procedural Programming II (2017.08.07)"
'''

import math
from openpyxl import *
from functools import reduce

def get_rawdata_from_excel(filename):
    wb = load_workbook('class_1.xlsx')
    ws = wb.active
    raw_data = {}
    gen = ws.rows
    for c1, c2 in gen:
        raw_data.update({c1.value : c2.value})
    return raw_data

def average(c):
	average = reduce(lambda a, b: a + b, c) / len(c)
	return average

def variance(a, b):
	variance = (reduce(lambda c, d: c + d, map(lambda e: (e - b)**2, a))) / len(a)
	# variance = (reduce(lambda c, d: c + d, map(lambda e, f: (e - f)**2, a, b))) / len(a)
		# Does not work because b is avrg, which is a single number, which is not iterable.
	return variance

def stn_dev(a):
	stn_dev = round(math.sqrt(a), 2)
	return stn_dev