# For finding the min sum I used the pseudo code provided in the project description. For help figuring out how to keep 
#    track of the actual coins, I studied and modified two examples found online: 
#    http://data.faridani.me/top-down-recursion-dynamic-programming-and-memoization-in-python/ 
#    & https://www.dotnetperls.com/recursion-python 
# I also worked with a friend to figure out how dictionaries work in python and returning multiple values since
#    the code also has to return an array of actual coins
def changeslow(denom_array, change_value):
    result1, result2 = helper_changeslow(change_value, denom_array)
    coins = [0] * len(denom_array)  
    for i in range(0, len(denom_array)):   
        if result2.has_key(denom_array[i]):       
            coins[i] = result2.get(denom_array[i])   
    return coins

def helper_changeslow(amount, coins):
    numcoins = 0
    results = {}
    #base cases
    if len(coins) == 1:
        numcoins =  amount / coins[0]
        results[coins[0]] = numcoins
    elif amount == 1:
        numcoins = 1
        results[coins[0]] = 1
    elif amount == 0: 
        numcoins = 0
    #recursive case
    else:
        if (amount - coins[-1]>= 0):
            solutionution1 = helper_changeslow(amount-coins[-1], coins)
            solutionution2 = helper_changeslow(amount, coins[:-1])
            numcoins += min(1+ solutionution1[0], solutionution2[0])
            #figure out the coins dictionary for return value
            if 1+ solutionution1[0]<solutionution2[0]:
                if coins[-1] in results:
                    results[coins[-1]] += 1
                else: 
                    results[coins[-1]] = 1
                results = { a: results.get(a, 0) + solutionution1[1].get(a, 0) for a in set(results) | set(solutionution1[1]) }
            else:
                results = { a: results.get(a, 0) + solutionution2[1].get(a, 0) for a in set(results) | set(solutionution2[1]) }
        else:
            solution = helper_changeslow(amount, coins[:-1])
            numcoins += solution[0]
            results = { a: results.get(a, 0) + solution[1].get(a, 0) for a in set(results) | set(solution[1]) }
    return (numcoins, results)