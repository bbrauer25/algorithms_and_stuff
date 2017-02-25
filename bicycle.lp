\* bicycle *\
Minimize
Time_to_bicycle_90_miles: t10 + t20 + t30
Subject To
Max_Calories: 180 t10 + 600 t20 + 1020 t30 <= 2000
Total_Miles: 10 t10 + 20 t20 + 30 t30 = 90
Bounds
t10 <= 9
t20 <= 4.5
t30 <= 3
End
