array = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41]
tiny_array = [1,2,3,4,5,6,7,8,9,10,11]

def quat_search(sortedArray, target):
	array_size = len(sortedArray)
	quarter_size = int(array_size/4)
	first_array = sortedArray[0:quarter_size]
	second_array = sortedArray[quarter_size: quarter_size * 2]
	third_array = sortedArray[quarter_size * 2: quarter_size * 3]
	fourth_array = sortedArray[quarter_size * 3: array_size]
	
	print "Input Array:"
	print(sortedArray)
	print "Subarrays:"
	print(first_array)
	print(second_array)
	print(third_array)
	print(fourth_array)
	
	if fourth_array[0] == target:
		print "found target: " + str(target)
		return target # base case
	elif target > fourth_array[0]:
		quat_search(fourth_array, target)
	elif target >= third_array[0]:
		quat_search(third_array, target)
	elif target >= second_array[0]:
		quat_search(second_array, target)
	elif target >= first_array[0]:
		quat_search(first_array, target)	
	
quat_search(tiny_array, 5)