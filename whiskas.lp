\* whiskas *\
Minimize
cost_of_ingredients_per_can_of_food: 0.013 x1 + 0.008 x2
Subject To
FatRequirement: 0.08 x1 + 0.1 x2 >= 6
FibreRequirement: 0.001 x1 + 0.005 x2 <= 2
PercentagesSum: x1 + x2 = 100
ProteinRequirement: 0.1 x1 + 0.2 x2 >= 8
SaltRequirement: 0.002 x1 + 0.005 x2 <= 0.4
Bounds
-inf <= x1 <= 100
-inf <= x2 <= 100
End
