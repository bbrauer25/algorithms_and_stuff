"""
def changeslow(amounts, goal, coins = [], highest = 0, sum = 0):
    # Base case
    if sum == goal:
        result = [] 
        if highest == amounts[(len(amounts)-1)]:
            result = []
            count = 0
            for amount in amounts:
                count = coins.count(amount)
                result.append(count)
                count = count + 1 
            print result
            print count
            return
        

    # Recursive case
    for value in amounts:
        if value >= highest:
            copy = coins[:]
            copy.append(value)
            if sum + value <= goal:
                changeslow(amounts, goal, copy, value, sum + value)
"""

def changeslow(amounts, goal):
    result = [0]*len(amounts)
    test_result = [0]*len(amounts)
    result[0] = goal # set denomination 1 to goal, maximum coins possible
    # Base case 
    if goal in amounts:
        for idx, a in enumerate(amounts):
            if a == goal:
                result[idx] = 1
                return result
    else:
    #Recursive case
        possible_coins = []
        for idx, value in enumerate(amounts):
            if value <= goal:
                test_result = changeslow(amounts, goal - value)
                test_result[idx] = test_result[idx] + 1
                if sum(test_result) < sum(result):
                    result = test_result
        print amounts
        print goal
        print result
        return result

amounts = [1, 5, 10, 25, 50]

print(changeslow(amounts, 51))

