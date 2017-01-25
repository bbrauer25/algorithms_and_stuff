import math
#run by "python project1.py" on command line

#define global variables/arrays here
input_arrays = []
#with open('MSS_TestProblems.txt') as inputs:
with open('MSS_Problems.txt') as inputs:
	for line in inputs:
		input_arrays.append(line.split())

print input_arrays

#our four functions

def enumerate(input_array):
	return {"sum": 123, "subarray": [1,2,3,4]}

def better_enumerate(input_array):
	return {"sum": "", "subarray": []}

def divide_and_conquer(input_array):
	return {"sum": "", "subarray": []}

def linear(input_array):
	return {"sum": "", "subarray": []}



#write results to file
with open('project1_results.txt', 'w') as p1_results:
	p1_results.write("Enumerate Results:\n")
	for a in input_arrays:
		enumerate_result = enumerate(a)
		p1_results.write("Input: " + str(a) + "\n")
		p1_results.write("Sum: " + str(enumerate_result["sum"]) + "\n")
		p1_results.write("Subarray: " + str(enumerate_result["subarray"]) + "\n\n")


