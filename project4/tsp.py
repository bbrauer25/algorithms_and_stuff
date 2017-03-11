import sys, getopt, sha
import csv
import math

#get input filename from command line input

filename = sys.argv[1]

def printUsage():
	print "Usage: " + sys.argv[0] + ' -f <filename with city indices and coordinates>'

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

#read input file into an array
#first value on a line is the index
#second value is the x coordinate
#third value is the y coordinate

cities = []

with open(filename) as inputs:
	for i, line in enumerate(inputs):
		city_array = line.split()
		cities.append({
			"city": int(city_array[0]),
			"x": int(city_array[1]),
			"y": int(city_array[2])
			})
	print cities	

#tsp algorithm
def tsp_nn(cities):
	#first compute distances for cities (n^2)
	distances = []
	for c1 in cities:
		city_dist = []
		for c2 in cities:
			city_dist.append(math.sqrt((c1["x"] - c2["x"]) ** 2 + (c1["y"] - c2["y"]) ** 2))
		distances.append(city_dist)
	#next iterate through cities choosing nearest neighbor
	length = 0
	travel_path = []
	temp_cities = list(cities)
	last_city_idx = 0
	travel_path.append(temp_cities.pop(0))
	while len(temp_cities) > 0:
		shortest_dist = sys.maxint 
		best_city_idx = 0
		for idx, c in enumerate(temp_cities):
			if distances[last_city_idx][c["city"]] < shortest_dist:
				shortest_dist = distances[last_city_idx][c["city"]]
				best_city_idx = idx
		length = length + shortest_dist
		last_city_idx = temp_cities[best_city_idx]["city"]
		travel_path.append(temp_cities.pop(best_city_idx))
	
	#last add the final return path to the first city
	length = length + distances[last_city_idx][0]
	travel_path.append(cities[0])
	return {
		"length": length,
		"travel_path": travel_path
	}

def tsp_nn_r(cities):
	#first compute distances for cities (n^2)
	distances = []
	for c1 in cities:
		city_dist = []
		for c2 in cities:
			city_dist.append(math.sqrt((c1["x"] - c2["x"]) ** 2 + (c1["y"] - c2["y"]) ** 2))
		distances.append(city_dist)
	shortest_length = sys.maxint
	shortest_travel_path = []
	#next do nearest neighbor for each vertex
	for j in range(len(cities)):
		temp_cities = list(cities)
		last_city_idx = 0
		travel_path = []
		length = 0
		travel_path.append(temp_cities.pop(j))
		while len(temp_cities) > 0:
			shortest_dist = sys.maxint
			best_city_idx = 0
			for idx, c in enumerate(temp_cities):
				if distances[last_city_idx][c["city"]] < shortest_dist:
					shortest_dist = distances[last_city_idx][c["city"]]
					best_city_idx = idx
			length = length + shortest_dist
			if length > shortest_length:
				break
			last_city_idx = temp_cities[best_city_idx]["city"]
			travel_path.append(temp_cities.pop(best_city_idx))
		#add the final return path to the first city
		length = length + distances[last_city_idx][j]
		travel_path.append(cities[j])
		if length < shortest_length:
			shortest_length = length
			shortest_travel_path = travel_path
	return {
		"length": shortest_length,
		"travel_path": shortest_travel_path
	}


#name output file as input file with ".tour" appended
output_file = filename + ".tour"
nn_result = tsp_nn(cities)
print nn_result
nnr_result = tsp_nn_r(cities)
print nnr_result
print "NN Result:" + str(nn_result["length"])
print "NNR Result: " + str(nnr_result["length"])
print nnr_result["length"] / 2579

with open(output_file, 'w') as output:
	output.write(str(nnr_result["length"]) + '\n')
	for c in nnr_result["travel_path"]:
		output.write(str(c["city"]) + '\n')
