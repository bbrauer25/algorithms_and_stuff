from pulp import *

prob = LpProblem("bicycle", LpMinimize)

#Variables
t10 = LpVariable("t10", 0, 9)
t20 = LpVariable("t20", 0, 4.5)
t30 = LpVariable("t30", 0, 3)

#Objective
prob += t10 + t20 + t30, "Time to bicycle 90 miles"

#Constraints
prob += t10 * 10 + t20 * 20 + t30 * 30 == 90, "Total Miles"
prob += t10 * 180 + t20 * 600 + t30 * 1020 <= 2000, "Max Calories"

prob.writeLP("bicycle.lp")

prob.solve()

print("Status: ", LpStatus[prob.status])

for v in prob.variables():
	print(v.name, " = ", v.varValue)

print("Total time traveled: ", value(prob.objective))