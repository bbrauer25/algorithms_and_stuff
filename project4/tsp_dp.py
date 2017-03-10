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
def tsp_dp(cities):
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

#name output file as input file with ".tour" appended
output_file = filename + ".tour"
result = tsp_dp(cities)
print result
print result["length"]

with open(output_file, 'w') as output:
	output.write(str(result["length"]) + '\n')
	for c in result["travel_path"]:
		output.write(str(c["city"]) + '\n')
