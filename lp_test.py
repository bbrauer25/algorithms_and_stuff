from pulp import *

prob = LpProblem("test1", LpMinimize) 

# Variables 
x = LpVariable("x", 0, 4) #LpContinuous or LpInteger
y = LpVariable("y", -1, 1) 
z = LpVariable("z", 0) 

# Objective 
prob += x + 4*y + 9*z 

# Constraints 
prob += x+y <= 5 
prob += x+z >= 10 
prob += -y+z == 7 

prob.solve() 

# Solution 
for v in prob.variables(): 
	print v.name, "=", v.varValue 

print "objective=", value(prob.objective)  


nprob = LpProblem("whiskas", LpMinimize) # or LpMaximize
x1 = LpVariable("x1", None, 100)
x2 = LpVariable("x2", None, 100)

#first add objective function

nprob += 0.013*x1 + 0.008*x2, "cost of ingredients per can of food"

#Constraints
nprob += x1 + x2 == 100, "PercentagesSum"
nprob += 0.100*x1 + 0.200*x2 >= 8.0, "ProteinRequirement"
nprob += 0.080*x1 + 0.100*x2 >= 6.0, "FatRequirement"
nprob += 0.001*x1 + 0.005*x2 <= 2.0, "FibreRequirement"
nprob += 0.002*x1 + 0.005*x2 <= 0.4, "SaltRequirement"

nprob.writeLP("whiskas.lp")

nprob.solve()

print("Status:", LpStatus[nprob.status])

for v in nprob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Ingredients per can = ", value(nprob.objective))


