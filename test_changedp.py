

def changedp(denom_array, change_value):
	coin_values = [0] * (change_value + 1)
	min_counts = [0] * (change_value + 1)
	for c in range(change_value + 1):
		num_coins = c
		coin_value = 1
		temp_coins = []
		for d in denom_array:
			if d <= c:
				temp_coins.append(d)
		for t in temp_coins:
			if min_counts[c - t] + 1 < num_coins:
				num_coins = min_counts[c - t] + 1
				coin_value = t
		min_counts[c] = num_coins
		coin_values[c] = coin_value
	print coin_values
	#figure out which coins make the minimum change
	result = [0]*len(denom_array)
	change_left = change_value
	while change_left > 0:
		coin_to_add = coin_values[change_left]
		for idx, d in enumerate(denom_array):
			if d == coin_to_add:
				result[idx] = result[idx] + 1
				break
		change_left = change_left - coin_to_add

	print denom_array
	print result
	print min_counts
	print min_counts[change_value]
	return min_counts[change_value]

def changedpcompact(denom_array, change_value):
	min_coins = [0] * (change_value + 1)
	current_coins = [0] * (change_value + 1)
	for c in range(change_value + 1):
		coins = c
		newCoin = 1
		for j in [d for d in denom_array if d <= c]:
		    if current_coins[c-j] + 1 < coins:
		       coins = current_coins[c-j]+1
		       newCoin = j
		current_coins[c] = coins
		min_coins[c] = newCoin
	print min_coins
	print current_coins
	print current_coins[change_value]
	return current_coins[change_value]

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   print coinsUsed
   print minCoins
   print minCoins[change]
   return minCoins[change]

amnt = 63
clist = [1,5,10,21,25]
coinsUsed = [0]*(amnt + 1)
coinCount = [0]*(amnt + 1)

changedpval = changedp(clist, amnt)
changedbcompactval = changedpcompact(clist, amnt)
dpmakechangeval = dpMakeChange(clist, amnt, coinCount, coinsUsed)

