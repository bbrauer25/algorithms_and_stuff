import math
from random import randint
import time
import sys, getopt, sha
import csv

#get input filename from command line input

filename = ""

def printUsage():
	print "Usage: " + sys.argv[0] + ' -f <filename with demoninations and change amounts>'

try:
	opts, args = getopt.getopt(sys.argv[1:], "hf:", [])
except getopt.GetoptError:
	printUsage()
	sys.exit(2)
for opt, arg in opts:
	print(opt)
	if opt == '-h':
		printUsage()
		sys.exit()
	elif opt == '-f':
		filename = arg

if filename == "":
	print "file name is required"
	printUsage()
	sys.exit(3)

#read input file into two arrays

denom_arrays = []
change_values = []

with open(filename) as inputs:
	for i, line in enumerate(inputs):
		if i % 2 == 0:
			sub_array = line.split()
			denom_arrays.append(map(int, sub_array))
		else:
			change_values.append(int(line))

print denom_arrays
print change_values


#our three functions

def changeslow(denom_array, change_value):
	time.sleep(1)
	return [1,1,1,1]

def changegreedy(denom_array, change_value):
	return [1,1,1,1]

def changedp(denom_array, change_value):
	return [1,1,1,1]



#write results of tests to file
write_file = filename[:-4] + "change.txt"
runtime_results = {"changeslow": [], "changegreedy": [], "changedp": []}

with open(write_file, 'w') as p2_results:

	p2_results.write("Algorithm changeslow:\n")
	for idx, d in enumerate(denom_arrays):
		#track runtime and write all results to dictionary
		start_time = time.time()
		result = changeslow(d, change_values[idx])
		time_elapsed = time.time() - start_time
		runtime_results["changeslow"].append({"denom_array": d, "change_value": change_values[idx], "coins": result, "runtime": time_elapsed, })
		#write to file per assignment format requirements
		for i in d:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		for i in result:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		p2_results.write(str(sum(result)) + '\n\n')

	p2_results.write("Algorithm changegreedy:\n")
	for idx, d in enumerate(denom_arrays):
		#track runtime and write all results to dictionary
		start_time = time.time()
		result = changegreedy(d, change_values[idx])
		time_elapsed = time.time() - start_time
		runtime_results["changegreedy"].append({"denom_array": d, "change_value": change_values[idx], "coins": result, "runtime": time_elapsed, })
		#write to file per assignment format requirements
		for i in d:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		for i in result:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		p2_results.write(str(sum(result)) + '\n\n')

	p2_results.write("Algorithm changedb\n")
	for idx, d in enumerate(denom_arrays):
		#track runtime and write all results to dictionary
		start_time = time.time()
		result = changedp(d, change_values[idx])
		time_elapsed = time.time() - start_time
		runtime_results["changedp"].append({"denom_array": d, "change_value": change_values[idx], "coins": result, "runtime": time_elapsed, })
		#write to file per assignment format requirements
		for i in d:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		for i in result:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		p2_results.write(str(sum(result)) + '\n\n')


#for now just print runtimes dictionary - we could use this stuff for analyses on writeup
#probably write some stuff to a csv file or something here eventually for analyses (number of coins, A, runtime)
print runtime_results





