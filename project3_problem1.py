from pulp import *

prob = LpProblem("transportation_a", LpMinimize) 

#Variables
route_names = ["p1w1", "p1w2", "p2w1", "p2w2", "p3w1", "p3w2", "p3w3", 
"p4w2", "p4w3", "w1r1", "w1r2", "w1r3", "w1r4", "w2r3", "w2r4", "w2r5", 
"w2r6", "w3r4", "w3r5", "w3r6", "w3r7"]

costs = {
	"p1w1": 10,
	"p1w2": 15,
	"p2w1": 11,
	"p2w2": 8,
	"p3w1": 13,
	"p3w2": 8,
	"p3w3": 9,
	"p4w2": 14,
	"p4w3": 8,
	"w1r1": 5,
	"w1r2": 6,
	"w1r3": 7,
	"w1r4": 10,
	"w2r3": 12,
	"w2r4": 8,
	"w2r5": 10,
	"w2r6": 14,
	"w3r4": 14,
	"w3r5": 12,
	"w3r6": 12,
	"w3r7": 6
}

routes = LpVariable.dicts("Rte", route_names, 0)

#Objective
#Minimize cost of shipping to warehouses and then to retailers
prob += lpSum([costs[r] * routes[r] for r in route_names]), "Total cost of shipping"

#Constraints
#Stay within the capacity of each plant
#Meet the demand for each retailer
#amount that goes in to a warehouse must go out to some combination of retailers
#Supply - p1: 150, p2: 450, p3: 250, p4: 150
#Demand - r1: 100, r2: 150, r3: 100, r4: 200, r5: 200, r6: 150, r7: 100

#Supply
prob += routes["p1w1"] + routes["p1w2"] <= 150, "P1 Capacity"
prob += routes["p2w1"] + routes["p2w2"] <= 450, "P2 Capacity"
prob += routes["p3w1"] + routes["p3w2"] + routes["p3w3"] <=250, "P3 Capacity"
prob += routes["p4w2"] + routes["p4w3"] <= 150, "P4 Capacity"
#Demand
prob += routes["w1r1"] >= 100, "R1 Demand"
prob += routes["w1r2"] >= 150, "R2 Demand"
prob += routes["w1r3"] + routes["w2r3"] >= 100, "R3 Demand"
prob += routes["w1r4"] + routes["w2r4"] + routes["w3r4"] >= 200, "R4 Demand"
prob += routes["w2r5"] + routes["w3r5"] >= 200, "R5 Demand"
prob += routes["w2r6"] + routes["w3r6"] >= 150, "R6 Demand"
prob += routes["w3r7"] >= 100, "R7 Demand"
#Warehouse equal flow
prob += routes["p1w1"] + routes["p2w1"] + routes["p3w1"] == routes["w1r1"] + routes["w1r2"] + routes["w1r3"] + routes["w1r4"], "W1 Flow"
prob += routes["p1w2"] + routes["p2w2"] + routes["p3w2"] + routes["p4w2"] == routes["w2r3"] + routes["w2r4"] + routes["w2r5"] + routes["w2r6"], "W2 Flow"
prob += routes["p3w3"] + routes["p4w3"] == routes["w3r4"] + routes["w3r5"] + routes["w3r6"] + routes["w3r7"], "W3 Flow"


prob.writeLP("transportation_a.lp")

prob.solve()

print("Part A Status: ", LpStatus[prob.status])

for v in prob.variables():
	print(v.name + ": " + str(v.varValue))

print("Total shipping cost: ", value(prob.objective))

#Part B - warehouse 2 closes

prob = LpProblem("transportation_b", LpMinimize) 

#Variables
route_names = ["p1w1", "p2w1", "p3w1", "p3w3", "p4w3", "w1r1", "w1r2", "w1r3", "w1r4", "w3r4", "w3r5", "w3r6", "w3r7"]

costs = {
	"p1w1": 10,
	"p2w1": 11,
	"p3w1": 13,
	"p3w3": 9,
	"p4w3": 8,
	"w1r1": 5,
	"w1r2": 6,
	"w1r3": 7,
	"w1r4": 10,
	"w3r4": 14,
	"w3r5": 12,
	"w3r6": 12,
	"w3r7": 6
}

routes = LpVariable.dicts("Rte", route_names, 0)

#Objective
#Minimize cost of shipping to warehouses and then to retailers
prob += lpSum([costs[r] * routes[r] for r in route_names]), "Total cost of shipping"

#Constraints
#Stay within the capacity of each plant
#Meet the demand for each retailer
#amount that goes in to a warehouse must go out to some combination of retailers
#Supply - p1: 150, p2: 450, p3: 250, p4: 150
#Demand - r1: 100, r2: 150, r3: 100, r4: 200, r5: 200, r6: 150, r7: 100

#Supply
prob += routes["p1w1"] <= 150, "P1 Capacity"
prob += routes["p2w1"] <= 450, "P2 Capacity"
prob += routes["p3w1"] + routes["p3w3"] <=250, "P3 Capacity"
prob += routes["p4w3"] <= 150, "P4 Capacity"
#Demand
prob += routes["w1r1"] >= 100, "R1 Demand"
prob += routes["w1r2"] >= 150, "R2 Demand"
prob += routes["w1r3"] >= 100, "R3 Demand"
prob += routes["w1r4"] + routes["w3r4"] >= 200, "R4 Demand"
prob += routes["w3r5"] >= 200, "R5 Demand"
prob += routes["w3r6"] >= 150, "R6 Demand"
prob += routes["w3r7"] >= 100, "R7 Demand"
#Warehouse equal flow
prob += routes["p1w1"] + routes["p2w1"] + routes["p3w1"] == routes["w1r1"] + routes["w1r2"] + routes["w1r3"] + routes["w1r4"], "W1 Flow"
#prob += routes["p1w2"] + routes["p2w2"] + routes["p3w2"] + routes["p4w2"] == routes["w2r3"] + routes["w2r4"] + routes["w2r5"] + routes["w2r6"], "W2 Flow"
prob += routes["p3w3"] + routes["p4w3"] == routes["w3r4"] + routes["w3r5"] + routes["w3r6"] + routes["w3r7"], "W3 Flow"


prob.writeLP("transportation_b.lp")

prob.solve()

print("Part B: Status with W2 Closed: ", LpStatus[prob.status])

for v in prob.variables():
	print(v.name, " = ", v.varValue)

print("Total shipping cost: ", value(prob.objective))

#Part C - warehouse 2 limited to 100 per week

prob = LpProblem("transportation_c", LpMinimize) 

#Variables
route_names = ["p1w1", "p1w2", "p2w1", "p2w2", "p3w1", "p3w2", "p3w3", 
"p4w2", "p4w3", "w1r1", "w1r2", "w1r3", "w1r4", "w2r3", "w2r4", "w2r5", 
"w2r6", "w3r4", "w3r5", "w3r6", "w3r7"]

costs = {
	"p1w1": 10,
	"p1w2": 15,
	"p2w1": 11,
	"p2w2": 8,
	"p3w1": 13,
	"p3w2": 8,
	"p3w3": 9,
	"p4w2": 14,
	"p4w3": 8,
	"w1r1": 5,
	"w1r2": 6,
	"w1r3": 7,
	"w1r4": 10,
	"w2r3": 12,
	"w2r4": 8,
	"w2r5": 10,
	"w2r6": 14,
	"w3r4": 14,
	"w3r5": 12,
	"w3r6": 12,
	"w3r7": 6
}

routes = LpVariable.dicts("Rte", route_names, 0)

#Objective
#Minimize cost of shipping to warehouses and then to retailers
prob += lpSum([costs[r] * routes[r] for r in route_names]), "Total cost of shipping"

#Constraints
#Stay within the capacity of each plant
#Meet the demand for each retailer
#amount that goes in to a warehouse must go out to some combination of retailers
#Supply - p1: 150, p2: 450, p3: 250, p4: 150
#Demand - r1: 100, r2: 150, r3: 100, r4: 200, r5: 200, r6: 150, r7: 100

#Supply
prob += routes["p1w1"] + routes["p1w2"] <= 150, "P1 Capacity"
prob += routes["p2w1"] + routes["p2w2"] <= 450, "P2 Capacity"
prob += routes["p3w1"] + routes["p3w2"] + routes["p3w3"] <=250, "P3 Capacity"
prob += routes["p4w2"] + routes["p4w3"] <= 150, "P4 Capacity"
#Demand
prob += routes["w1r1"] >= 100, "R1 Demand"
prob += routes["w1r2"] >= 150, "R2 Demand"
prob += routes["w1r3"] + routes["w2r3"] >= 100, "R3 Demand"
prob += routes["w1r4"] + routes["w2r4"] + routes["w3r4"] >= 200, "R4 Demand"
prob += routes["w2r5"] + routes["w3r5"] >= 200, "R5 Demand"
prob += routes["w2r6"] + routes["w3r6"] >= 150, "R6 Demand"
prob += routes["w3r7"] >= 100, "R7 Demand"
#Warehouse equal flow
prob += routes["p1w1"] + routes["p2w1"] + routes["p3w1"] == routes["w1r1"] + routes["w1r2"] + routes["w1r3"] + routes["w1r4"], "W1 Flow"
prob += routes["p1w2"] + routes["p2w2"] + routes["p3w2"] + routes["p4w2"] == routes["w2r3"] + routes["w2r4"] + routes["w2r5"] + routes["w2r6"], "W2 Flow"
prob += routes["p3w3"] + routes["p4w3"] == routes["w3r4"] + routes["w3r5"] + routes["w3r6"] + routes["w3r7"], "W3 Flow"
prob += routes["p1w2"] + routes["p2w2"] + routes["p3w2"] + routes["p4w2"] <= 100, "W2 Capacity"

prob.writeLP("transportation_c.lp")

prob.solve()

print("Status: ", LpStatus[prob.status])

for v in prob.variables():
	print(v.name + ": " + str(v.varValue))

print("Total shipping cost: ", value(prob.objective))



