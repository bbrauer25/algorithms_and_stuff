import math
from random import randint
import time
import time

#run by "python project1.py" on command line

input_arrays = []
#switch to test problem set if desired
#with open('MSS_TestProblems.txt') as inputs:
with open('MSS_Problems.txt') as inputs:
	for line in inputs:
		input_arrays.append(line.split())

print input_arrays

#our four functions

def enumerate(input_array):
	#code here!
	return {"sum": 123, "subarray": [1,2,3,4]}

def better_enumerate(input_array):
	#code here!
	return {"sum": 123, "subarray": [1,2,3,4]}

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

def linear(input_array):
	#code here!
	return {"sum": 123, "subarray": [1,2,3,4]}


#write results of tests to file
with open('MSS_Results.txt', 'w') as p1_results:
	p1_results.write("Enumerate Results:\n")
	for a in input_arrays:
		result = enumerate(a)
		p1_results.write("Input: " + str(a) + "\n")
		p1_results.write("Sum: " + str(result["sum"]) + "\n")
		p1_results.write("Subarray: " + str(result["subarray"]) + "\n\n")
	p1_results.write("Better Enumerate Results:\n")
	for a in input_arrays:
		result = better_enumerate(a)
		p1_results.write("Input: " + str(a) + "\n")
		p1_results.write("Sum: " + str(result["sum"]) + "\n")
		p1_results.write("Subarray: " + str(result["subarray"]) + "\n\n")
	p1_results.write("Divide and Conquer Results:\n")
	for a in input_arrays:
		result = divide_and_conquer(a, 0, len(a))
		p1_results.write("Input: " + str(a) + "\n")
		p1_results.write("Sum: " + str(result["sum"]) + "\n")
		p1_results.write("Subarray: " + str(result["subarray"]) + "\n\n")
	p1_results.write("Linear Results:\n")
	for a in input_arrays:
		result = linear(a)
		p1_results.write("Input: " + str(a) + "\n")
		p1_results.write("Sum: " + str(result["sum"]) + "\n")
		p1_results.write("Subarray: " + str(result["subarray"]) + "\n\n")

#Time testing:
#array to set number of elements in the 10 input arrays, and to store timing results
#we may need to change the number of elements here to get reasonable results
num_elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
enum_times = []
better_enum_times = []
d_and_c_times = []
linear_times = []

for n in num_elements:
	a = []
	for _ in range(n):
		a.append(randint(-100, 100))
	print a

	start_time = time.time()
	result = enumerate(a)
	time_elapsed = time.time() - start_time
	enum_times.append(time_elapsed)

	start_time = time.time()
	result = better_enumerate(a)
	time_elapsed = time.time() - start_time
	better_enum_times.append(time_elapsed)

	start_time = time.time()
	result = divide_and_conquer(a, 0, len(a))
	time_elapsed = time.time() - start_time
	d_and_c_times.append(time_elapsed)

	start_time = time.time()
	results = linear(a)
	time_elapsed = time.time() - start_time
	linear_times.append(time_elapsed)

with open("runtime_results.txt", 'w') as rt_results:
	rt_results.write("Enum Times: \n")
	rt_results.write(enum_times)
	rt_results.write("\nBetter Enum Times:\n")
	rt_results.write(better_enum_times)
	rt_results.write("\nDivide and conquer times: \n")
	rt_results.write(d_and_c_times)
	rt_results.write("\nLinear Times: \n")
	rt_results.write(linear_times)

	print enum_times
	print better_enum_times
	print d_and_c_times
	print linear_times







