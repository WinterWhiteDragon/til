def binary_search(data, target):
	data.sort()
	start = 0
	end = len(data) -1
	
	while start <= end:
		mid = (end + start) // 2
		if data[mid] == target:
			return mid
		elif data[mid] > target:
			end = mid - 1
		elif data[mid] < target:
			start = mid + 1
	return None


lis = [7, 1, 55, 66, 2, 3]
idx = binary_search(lis, 66)
if idx:
	print("The target is at index {} and it's value is {}".format(idx, lis[idx]))
else:
	print("Data not found")