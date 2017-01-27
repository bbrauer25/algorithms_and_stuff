
#test_array  = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
#test_array = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2]
#test_array = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19] 
test_array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84] 



def divide_and_conquer(input_array, low, high):
	#low and high track the current actual indices of the original array

	print(input_array)

	if len(input_array) == 1:
		return {"sum": input_array[0], "low_index": low, "high_index": high}

	mid_point = int(len(input_array)/2)

	left_result = divide_and_conquer(input_array[0:mid_point], low, mid_point - 1)
	right_result = divide_and_conquer(input_array[mid_point:len(input_array)], mid_point, high)
	max_left = left_result["sum"]
	max_right = right_result["sum"]

	n = mid_point - 1
	sum = 0
	right_sum = 0
	left_sum = 0 #lowest possible random 
	low_index = low
	high_index = high

	while (n >= 0):
		sum = sum + input_array[n]
		if sum > left_sum:
			left_sum = sum
			low_index = low + n
		n = n - 1

	sum = 0
	n = mid_point
	while (n < len(input_array)):
		sum = sum + input_array[n]
		if sum > right_sum:
			right_sum = sum
			high_index = low + n
		n = n + 1

	mid_sum = left_sum + right_sum


	print("left_sum: " + str(max_left))
	print("right_sum: " + str(max_right))
	print("mid_sum: " + str(mid_sum))
	print("low_index: " + str(low_index))
	print("high_index: " + str(high_index))
	#TO DO - figure out how to print proper values if left or right side wins

	if (max(max_left, max_right, mid_sum) == max_left):
		return {"sum": max_left, "low_index": left_result["low_index"], "high_index": left_result["high_index"]}
	elif (max(max_left, max_right, mid_sum) == max_right):
		return {"sum": max_right, "low_index": right_result["low_index"], "high_index": right_result["high_index"]}
	else:
		return {"sum": mid_sum, "low_index": low_index, "high_index": high_index}

print(divide_and_conquer(test_array, 0, len(test_array)))