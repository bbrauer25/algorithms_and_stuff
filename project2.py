import math
from random import randint
import time
import sys, getopt, sha
import csv

#get input filename from command line input

filename = sys.argv[1] + ".txt"

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

# For finding the min sum I used the pseudo code provided in the project description. For help figuring out how to keep 
#    track of the actual coins, I studied and modified two examples found online: 
#    http://data.faridani.me/top-down-recursion-dynamic-programming-and-memoization-in-python/ 
#    & https://www.dotnetperls.com/recursion-python 
# I also worked with a friend to figure out how dictionaries work in python and returning multiple values since
#    the code also has to return an array of actual coins
def changeslow(denom_array, change_value):
    result1, result2 = helper_changeslow(change_value, denom_array)
    coins = [0] * len(denom_array)  
    for i in range(0, len(denom_array)):   
        if result2.has_key(denom_array[i]):       
            coins[i] = result2.get(denom_array[i])   
    return coins

def helper_changeslow(amount, coins):
    numcoins = 0
    results = {}
    #base cases
    if len(coins) == 1:
        numcoins =  amount / coins[0]
        results[coins[0]] = numcoins
    elif amount == 1:
        numcoins = 1
        results[coins[0]] = 1
    elif amount == 0: 
        numcoins = 0
    #recursive case
    else:
        if (amount - coins[-1]>= 0):
            solutionution1 = helper_changeslow(amount-coins[-1], coins)
            solutionution2 = helper_changeslow(amount, coins[:-1])
            numcoins += min(1+ solutionution1[0], solutionution2[0])
            #figure out the coins dictionary for return value
            if 1+ solutionution1[0]<solutionution2[0]:
                if coins[-1] in results:
                    results[coins[-1]] += 1
                else: 
                    results[coins[-1]] = 1
                results = { a: results.get(a, 0) + solutionution1[1].get(a, 0) for a in set(results) | set(solutionution1[1]) }
            else:
                results = { a: results.get(a, 0) + solutionution2[1].get(a, 0) for a in set(results) | set(solutionution2[1]) }
        else:
            solution = helper_changeslow(amount, coins[:-1])
            numcoins += solution[0]
            results = { a: results.get(a, 0) + solution[1].get(a, 0) for a in set(results) | set(solution[1]) }
    return (numcoins, results)

def changegreedy(denom_array, change_value):
	outArr = [0] * len(denom_array)
	for i in range(len(denom_array)-1,-1,-1):
		while(change_value >= denom_array[i]):
			outArr[i] += 1
			change_value -= denom_array[i]
	return outArr

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
		print d
		print change_values[idx]
		print result
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
		print d
		print change_values[idx]
		print result
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
		print d
		print change_values[idx]
		print result
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

#changeslow_a = [227, 347, 461, 599, 727]
changeslow_a = [20, 40, 60, 80, 100]
#changeslow_a = [109, 127, 139, 151, 163]

p3a = []
a = 2010
while a <= 2200:
	p3a.append(a)
	a = a + 5

p4and5a = []
a = 2000
while a <= 2500:
	p4and5a.append(a)
	a = a + 1

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

for a in p4and5a:
	start_time = time.time()
	result = changedp(p4v1, a)
	time_elapsed = time.time() - start_time
	results["changedp"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p4v1})
	start_time = time.time()
	result = changegreedy(p4v1, a)
	time_elapsed = time.time() - start_time
	results["changegreedy"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p4v1})
	start_time = time.time()
	result = changedp(p4v2, a)
	time_elapsed = time.time() - start_time
	results["changedp"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p4v2})
	start_time = time.time()
	result = changegreedy(p4v2, a)
	time_elapsed = time.time() - start_time
	results["changegreedy"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p4v2})
	start_time = time.time()
	result = changedp(p5v, a)
	time_elapsed = time.time() - start_time
	results["changedp"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p5v})
	start_time = time.time()
	result = changegreedy(p5v, a)
	time_elapsed = time.time() - start_time
	results["changegreedy"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p5v})


#run change slow
for a in changeslow_a:
	start_time = time.time()
	result = changeslow(p3v, a)
	time_elapsed = time.time() - start_time
	print result
	results["changeslow"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p3v})
	start_time = time.time()
	result = changeslow(p4v1, a)
	time_elapsed = time.time() - start_time
	print result
	results["changeslow"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p4v1})
	start_time = time.time()
	result = changeslow(p4v2, a)
	time_elapsed = time.time() - start_time
	print result
	results["changeslow"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p4v2})
	start_time = time.time()
	result = changeslow(p5v, a)
	time_elapsed = time.time() - start_time
	print result
	results["changeslow"].append({"change_value": a, "num_coins": sum(result), "runtime": time_elapsed, "coins": result, "denominations": p5v})


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






