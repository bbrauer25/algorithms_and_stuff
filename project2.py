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


#our three functions

def changeslow(denom_array, change_value):
	return [1,1,1,1]

def changegreedy(denom_array, change_value):
	return [1,1,1,1]

def changedp(denom_array, change_value):
	coin_values = [0] * (change_value + 1)
	min_counts = [0] * (change_value + 1)
	for c in range(change_value + 1):
		num_coins = c
		coin_value = 1
		temp_coins = []
		for d in denom_array:
			if d <= c:
				temp_coins.append(d)
		for t in temp_coins:
			if min_counts[c - t] + 1 < num_coins:
				num_coins = min_counts[c - t] + 1
				coin_value = t
		min_counts[c] = num_coins
		coin_values[c] = coin_value
	print coin_values
	#figure out which coins make the minimum change
	result = [0]*len(denom_array)
	change_left = change_value
	while change_left > 0:
		coin_to_add = coin_values[change_left]
		for idx, d in enumerate(denom_array):
			if d == coin_to_add:
				result[idx] = result[idx] + 1
				break
		change_left = change_left - coin_to_add

	print denom_array
	print result
	return result



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
		runtime_results["changeslow"].append({"change_value": change_values[idx], "num_coins": sum(result), "runtime": time_elapsed, })
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
		runtime_results["changegreedy"].append({"change_value": change_values[idx], "num_coins": sum(result), "runtime": time_elapsed, })
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
		runtime_results["changedp"].append({"change_value": change_values[idx], "num_coins": sum(result), "runtime": time_elapsed, })
		#write to file per assignment format requirements
		for i in d:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		for i in result:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		p2_results.write(str(sum(result)) + '\n\n')


#write runtimes, change value (A) and number of coins to csv file for analyses
print runtime_results
with open('changegreedy_results.csv', 'w') as rt_csv:
	fieldnames = ['change_value', 'num_coins', 'runtime']
	writer = csv.DictWriter(rt_csv, fieldnames=fieldnames)

	writer.writeheader()
	for r in runtime_results["changegreedy"]:
		writer.writerow(r)

with open('changedp_results.csv', 'w') as rt_csv:
	fieldnames = ['change_value', 'num_coins', 'runtime']
	writer = csv.DictWriter(rt_csv, fieldnames=fieldnames)

	writer.writeheader()
	for r in runtime_results["changedp"]:
		writer.writerow(r)



