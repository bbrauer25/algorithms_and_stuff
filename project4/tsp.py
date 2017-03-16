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

#read input file into an array of dicts, one for each city
#first value on a line is the index - mapped to "city"
#second value is the x coordinate - mapped to "x"
#third value is the y coordinate = mapped to "y"

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

#tsp algorithm, nearest neighbor
def tsp_nn(cities):
	#first compute distances for cities (n^2)
	#store in a 2D array "distances"
	#where each subarray distance[i] contains the distances from city i to all other cities
	distances = []
	for c1 in cities:
		city_dist = []
		for c2 in cities:
			city_dist.append(int(round(math.sqrt((c1["x"] - c2["x"]) ** 2 + (c1["y"] - c2["y"]) ** 2))))
		distances.append(city_dist)
	#next iterate through cities choosing nearest neighbor
	length = 0 #distance of travel path
	travel_path = [] #sequence of travel path
	temp_cities = list(cities) #temporary copy of cities, each closest city will be popped in sequence
	last_city_idx = 0 #the index, in the cities array, of the last city added to temp_cities
	travel_path.append(temp_cities.pop(0)) #start with city at index 0
	#loop, find the nearest city, pop and add to temp_cities, add distance to length
	#iterate until no more cities remain in temp_cities array
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
	#travel_path.append(cities[0])
	return {
		"length": length,
		"travel_path": travel_path
	}

def tsp_nn_r(cities):
	#first compute distances for cities (n^2)
	#store in a 2D array "distances"
	#where each subarray distance[i] contains the distances from city i to all other cities
	distances = []
	for c1 in cities:
		city_dist = []
		for c2 in cities:
			city_dist.append(int(round(math.sqrt((c1["x"] - c2["x"]) ** 2 + (c1["y"] - c2["y"]) ** 2))))
		distances.append(city_dist)
	shortest_length = sys.maxint #update this each time a shorter travel path is found
	shortest_travel_path = [] #update this each time a shorter path is found
	#next do nearest neighbor for each vertex
	for j in range(len(cities)):
		print "running NN-R starting at city: " + str(j)
		temp_cities = list(cities)
		last_city_idx = j
		travel_path = []
		length = 0
		travel_path.append(temp_cities.pop(j))
		#loop, find the nearest city, pop and add to temp_cities, add distance to length
		#iterate until no more cities remain in temp_cities array
		while len(temp_cities) > 0:
			shortest_dist = sys.maxint
			best_city_idx = 0
			for idx, c in enumerate(temp_cities):
				if distances[last_city_idx][c["city"]] < shortest_dist:
					shortest_dist = distances[last_city_idx][c["city"]]
					best_city_idx = idx
			length = length + shortest_dist
			if length > shortest_length:
				print "length exceeds shortest distance: " + str(length)
				break
			last_city_idx = temp_cities[best_city_idx]["city"]
			travel_path.append(temp_cities.pop(best_city_idx))
		#add the final return path to the first city
		length = length + distances[last_city_idx][j]
		print "new shortest length: " + str(length)
		#travel_path.append(cities[j])
		if length < shortest_length:
			shortest_length = length
			shortest_travel_path = travel_path

	return {
		"length": shortest_length,
		"travel_path": shortest_travel_path
	}


##### CHEAPEST LINK ##############################
# 1. Order edges by ascending weight
# 2. Go through the edges except for the following
#	a. vertices may only utilize 2 edges 
#	b. the edges do not prematurely close the circuit
#
##################################################
def cheapestLink(cities):
	total = 0
	visited = [0] * len(cities) 
	distances = {}
	usedEdges =[]
	# Iterate through city combinations
	# Put edges into dictionary of Key: weight - Value: (city a,city b) tuple
	for c1 in cities:
		city_dist = []
		for c2 in cities:
			weight = int(round(math.sqrt((c1["x"] - c2["x"]) ** 2 + (c1["y"] - c2["y"]) ** 2)))
			edge = (c1["city"],c2["city"])
			if not distances.has_key(weight) and weight != 0:
				distances[weight] = edge
	
	# Sort edge dictionary
	sd = collections.OrderedDict(sorted(distances.items()))	
	
		# Iterate through sorted edges
		for d in sd:
			# Check if cities attached to edges have been touched
			# more than less than 2 time (valid for connection)
			# also check to see if this is a pre-mature circuit
			if visited[sd[d][0]] < 2 and visited[sd[d][1]] < 2:  #<------ Need to add check at or within this if to figure out if premature loop
				visited[sd[d][0]]+=1
				visited[sd[d][1]]+=1
				usedEdges.append(sd[d])
				# Increment Total since this is now a travelled distance
				total += d
		
		print visited		#<------ Somehow
		print usedEdges 	#<------ use this to
		print total		#<------ find answer
	
	
	
	
	
#name output file as input file with ".tour" appended
#if more than 2000 cities, only use nearest neighbor
#if less than 2000 cities, use repeated nearest neighbor
output_file = filename + ".tour"
if (len(cities) < 1000):
	nnr_result = tsp_nn_r(cities)
	print nnr_result
	print "NNR Result: " + str(nnr_result["length"])
	with open(output_file, 'w') as output:
		output.write(str(int(nnr_result["length"])) + '\n')
		for c in nnr_result["travel_path"]:
			output.write(str(c["city"]) + '\n')
else:
	nn_result = tsp_nn(cities)
	print nn_result
	print "NN Result:" + str(nn_result["length"])
	with open(output_file, 'w') as output:
		output.write(str(int(nn_result["length"])) + '\n')
		for c in nn_result["travel_path"]:
			output.write(str(c["city"]) + '\n')



