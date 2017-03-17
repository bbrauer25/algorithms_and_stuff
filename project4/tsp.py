import sys, getopt, sha
import csv
import math
import time
import copy


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

def tsp_cl(cities):
	input_edges = []
	temp_cities = list(cities)
	temp_cities.pop(0)
	path = []
	for c1 in cities:
		for c2 in temp_cities:
			distance = int(round(math.sqrt((c1["x"] - c2["x"]) ** 2 + (c1["y"] - c2["y"]) ** 2)))
			input_edges.append({"c1": c1["city"], "c2": c2["city"], "length": distance})
		if len(temp_cities) > 0:
			temp_cities.pop(0)
	sorted_edges = sorted(input_edges, key=lambda k: k['length']) 
	#add edges to array sorting travel paths
	used_edges = [[] for _ in range(len(cities))]
	for s in sorted_edges:
		#check if adding edge will result in more than 2 edges at either node
			if len(used_edges[s["c1"]]) < 2 and len(used_edges[s["c2"]]) < 2:
				#check if there is completed circuit formed
				used_edges[s["c1"]].append(s)
				used_edges[s["c2"]].append(s)
				#check circuit returns true if no circuit found
				path = check_circuit(used_edges, s["c1"])
				if path == 0:
					used_edges[s["c1"]].pop()
					used_edges[s["c2"]].pop()
	#find start city (one of two that only have 1 edge)
	start_city = 0
	for idx, u in enumerate(used_edges):
		if len(u) == 1:
			start_city = idx
			break
	#run path one more time to get final path from start city
	path = check_circuit(used_edges, start_city)
	path_dict = []
	#construct return value (dict with length and travel path of edges)
	path_dict.append(cities[path[0]])
	length = 0
	path.pop(0)
	for p in path:
		dx = path_dict[-1]["x"] - cities[p]["x"]
		dy = path_dict[-1]["y"] - cities[p]["y"]
		length = length + int(round(math.sqrt(dx*dx + dy*dy)))
		path_dict.append(cities[p])
	#add length of last return path to start city
	dx = path_dict[-1]["x"] - cities[start_city]["x"]
	dy = path_dict[-1]["y"] - cities[start_city]["y"]
	length = length + int(round(math.sqrt(dx*dx + dy*dy)))
	return {
		"length": length,
		"travel_path": path_dict
	}

#check if there is a completed circuit within an list of nodes, 
#where each node is itself an array of edges from that node, where each edge
#is a dictionary with "length", "c1", "c2", where c1 and c2 are integer values of cities
#[
#[{10, 1, 3}, {15, 5, 2}],
#[{15, 1, 2}]
#]
#start node is c1
def check_circuit(nodes, start_node):
	#list to track whether each node in nodes has been visited
	temp_nodes = copy.deepcopy(nodes)
	visited_nodes = [0] * len(nodes) #1 if visited, 0 if not
	#first go forward
	current_node = start_node
	visited_nodes[start_node] = 1
	path = []
	path.append(current_node)
	more_edges = True
	while more_edges:
		#make sure current node has other nodes to connect to
		if len(temp_nodes[current_node]) > 0:
			#update visited edges, check if current node is c1 or c2
			if temp_nodes[current_node][0]["c1"] == current_node:
				next_node = temp_nodes[current_node][0]["c2"]
			else:
				next_node = temp_nodes[current_node][0]["c1"]
			#check for circuit (next node already == 1)
			if visited_nodes[next_node] == 1:
				return 0 #fails if circuit found	
			visited_nodes[next_node] = 1
			#pop edges for both nodes matching that edge
			temp_nodes[current_node].pop(0)
			if temp_nodes[next_node][0]["c1"] == current_node or temp_nodes[next_node][0]["c2"] == current_node:
				temp_nodes[next_node].pop(0)
			else:
				temp_nodes[next_node].pop(1)
			#update current node
			current_node = next_node
			path.append(next_node)
		else:
			more_edges = False
	#next go backwards
	current_node = start_node
	while more_edges:
		#make sure current node has other nodes to connect to
		if len(temp_nodes[current_node]) > 0:
			#update visited edges, check if current node is c1 or c2
			if temp_nodes[current_node][0]["c1"] == current_node:
				next_node = temp_nodes[current_node][0]["c2"]
			else:
				next_node = temp_nodes[current_node][0]["c1"]
			#check for circuit (next node already == 1)
			if visited_nodes[next_node] == 1:
				return 0 #fails if circuit found	
			visited_nodes[next_node] = 1
			#pop edges for both nodes matching that edge
			temp_nodes[current_node].pop(0)
			if temp_nodes[next_node][0]["c1"] == current_node or temp_nodes[next_node][0]["c2"] == current_node:
				temp_nodes[next_node].pop(0)
			else:
				temp_nodes[next_node].pop(1)
			#update current node
			current_node = next_node
			path.insert(0, next_node)
		else:
			more_edges = False
	return path


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
	print distances
	sd = collections.OrderedDict(sorted(distances.items()))	
	print sd #orderectdict of (weight, (c1, c2))
	
	"""
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
	"""
	return "hi"
	

	
	
	
	
#name output file as input file with ".tour" appended
#if more than 2000 cities, only use nearest neighbor
#if less than 2000 cities, use repeated nearest neighbor
output_file = filename + ".tour"
start_time = time.time()

#choose whether to try nn_r
if (len(cities) <= 500):
	nnr_result = tsp_nn_r(cities)
	print nnr_result
	print "NNR Result: " + str(nnr_result["length"])
	with open(output_file, 'w') as output:
		output.write(str(int(nnr_result["length"])) + '\n')
		for c in nnr_result["travel_path"]:
			output.write(str(c["city"]) + '\n')
elif (len(cities) <= 2000):
	#try cl and nn
	cl_result = tsp_cl(cities)
	print cl_result
	print "CL Result: " + str(cl_result["length"])
	with open(output_file, 'w') as output:
		output.write(str(int(cl_result["length"])) + '\n')
		for c in cl_result["travel_path"]:
			output.write(str(c["city"]) + '\n')
else:
	nn_result = tsp_nn(cities)
	print nn_result
	print "NN Result: " + str(nn_result["length"])
	#store shortest path of one method or the other
	with open(output_file, 'w') as output:
		output.write(str(int(nn_result["length"])) + '\n')
		for c in nn_result["travel_path"]:
			output.write(str(c["city"]) + '\n')

print "Time Elapsed: " + str(time.time() - start_time)



