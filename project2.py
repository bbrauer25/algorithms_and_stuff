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
	return result

#write results of tests to file
write_file = filename[:-4] + "change.txt"

with open(write_file, 'w') as p2_results:

	p2_results.write("Algorithm changeslow:\n")
	for idx, d in enumerate(denom_arrays):
		result = changeslow(d, change_values[idx])
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
		result = changegreedy(d, change_values[idx])
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
		result = changedp(d, change_values[idx])
		#write to file per assignment format requirements
		for i in d:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		for i in result:
			p2_results.write(str(i) + ' ')
		p2_results.write('\n')
		p2_results.write(str(sum(result)) + '\n\n')


#construct V denominations array, and A array of different change values
#for project exercises 3-5

p3v = [1, 5, 10, 25, 50]
p4v1 = [1, 2, 6, 12, 24, 48, 60]
p4v2 = [1, 6, 13, 37, 150]
p5v = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

p3a = []
a = 2010
while a <= 2200:
	p3a.append(a)
	a = a + 5

p4a = []
a = 2000
while a <= 2200:
	p4a.append(a)
	a = a + 1

p5a = p4a

#run 3 algorithms and write results to files for each algorithm
results = {"changeslow": [], "changegreedy": [], "changedp": []}

#problem 3 run for each value of a for each algorithm
for a in p3a:
	start_time = time.time()
	result = changedp(p3v, a)
	time_elapsed = time.time() - start_time
	results["changedp"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p3v})
	start_time = time.time()
	result = changegreedy(p3v, a)
	time_elapsed = time.time() - start_time
	results["changegreedy"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p3v})
	start_time = time.time()
	result = changeslow(p3v, a)
	time_elapsed = time.time() - start_time
	results["changeslow"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p3v})

#TO DO: problems 4a, 4b, 5 

#write runtimes, change value (A) and number of coins to csv file for analyses
with open('changedp_results.csv', 'w') as rt_csv:
	fieldnames = ['change_value', 'num_coins', 'runtime', 'coins', 'denominations']
	writer = csv.DictWriter(rt_csv, fieldnames=fieldnames)

	writer.writeheader()
	for r in results["changedp"]:
		writer.writerow(r)

with open('changegreedy_results.csv', 'w') as rt_csv:
	fieldnames = ['change_value', 'num_coins', 'runtime', 'coins', 'denominations']
	writer = csv.DictWriter(rt_csv, fieldnames=fieldnames)

	writer.writeheader()
	for r in results["changegreedy"]:
		writer.writerow(r)

with open('changeslow_results.csv', 'w') as rt_csv:
	fieldnames = ['change_value', 'num_coins', 'runtime', 'coins', 'denominations']
	writer = csv.DictWriter(rt_csv, fieldnames=fieldnames)

	writer.writeheader()
	for r in results["changeslow"]:
		writer.writerow(r)






