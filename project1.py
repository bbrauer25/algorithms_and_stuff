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

def divide_and_conquer(input_array):
	#code here!
	return {"sum": 123, "subarray": [1,2,3,4]}

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
		result = divide_and_conquer(a)
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
	result = divide_and_conquer(a)
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







