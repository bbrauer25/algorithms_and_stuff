array = [4, -5, 29, 11, -17, 6, 10, -3, 12]

def min_and_max(a):
	if len(a) == 1:
		return {"min": a[0], "max": a[0]}
	elif len(a) == 2:
		if a[0] <= a[1]:
			return {"min": a[0], "max": a[1]}
		else:
			return {"min": a[1], "max": a[0]}
	elif len(a) > 2: #more than 2 elements in array
		min_max = {"min": a[0], "max": a[0]}
		k = int(len(a)/2)
		first_half_min_max = min_and_max(a[0:k])
		second_half_min_max = min_and_max(a[k:len(a)])
		if first_half_min_max["min"] < second_half_min_max["min"]:
			min_max["min"] = first_half_min_max["min"]
		else:
			min_max["min"] = second_half_min_max["min"]
		if first_half_min_max["max"] > second_half_min_max["max"]:
			min_max["max"] = first_half_min_max["max"]
		else:
			min_max["max"] = second_half_min_max["max"]
		return min_max
		
print "Running min and max for this array:"
print array
print(min_and_max(array))

