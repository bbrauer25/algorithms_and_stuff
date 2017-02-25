\* transportation_b *\
Minimize
Total_cost_of_shipping: 10 Rte_p1w1 + 11 Rte_p2w1 + 13 Rte_p3w1 + 9 Rte_p3w3
 + 8 Rte_p4w3 + 5 Rte_w1r1 + 6 Rte_w1r2 + 7 Rte_w1r3 + 10 Rte_w1r4
 + 14 Rte_w3r4 + 12 Rte_w3r5 + 12 Rte_w3r6 + 6 Rte_w3r7
Subject To
P1_Capacity: Rte_p1w1 <= 150
P2_Capacity: Rte_p2w1 <= 450
P3_Capacity: Rte_p3w1 + Rte_p3w3 <= 250
P4_Capacity: Rte_p4w3 <= 150
R1_Demand: Rte_w1r1 >= 100
R2_Demand: Rte_w1r2 >= 150
R3_Demand: Rte_w1r3 >= 100
R4_Demand: Rte_w1r4 + Rte_w3r4 >= 200
R5_Demand: Rte_w3r5 >= 200
R6_Demand: Rte_w3r6 >= 150
R7_Demand: Rte_w3r7 >= 100
W1_Flow: Rte_p1w1 + Rte_p2w1 + Rte_p3w1 - Rte_w1r1 - Rte_w1r2 - Rte_w1r3
 - Rte_w1r4 = 0
W3_Flow: Rte_p3w3 + Rte_p4w3 - Rte_w3r4 - Rte_w3r5 - Rte_w3r6 - Rte_w3r7 = 0
End
