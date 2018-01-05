"""
solutions to problems in EPI
"""


#naive recursion
def cc(n, denoms):
	minCoins =100
	globalMin =100
	if n == 0:
		return 0
	for a in denoms:
		if a <= n:
			globalMin = min(1+cc(n-a, denoms), globalMin)
		#if minCoins < globalMin:
			#globalMin= minCoins
	return globalMin

print(cc(5, [1, 5, 10, 25]))
print(cc(33, [1, 5, 10, 25]))

# greedy algorithm, always pick the largest possible coin, subtract from n
def greedyCC(n, denoms):
	prev =0
	count =0
	while n != 0:
		n -= max(denoms) if max(denoms)<n 
		count +=1 
	return count




"""
8/14/17
Find the number of ways to make change, given an amount change and 
an array of denominations, coins.
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""
def numberWaysMakeChange(change, coins):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    memo = [[0 for x in range(len(coins))] for _ in range(change+1)]
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(len(coins)):
        memo[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, change+1):
        for j in range(len(coins)):
            # x is number of ways if using coin[j]
            x = memo[i - coins[j]][j] if i-coins[j] >= 0 else 0
 
            # number of ways without using coin[j]
            y = memo[i][j-1] if j >= 1 else 0
 
            # total count
            memo[i][j] = x + y
 
    return memo[-1][-1]
#print(numberWaysMakeChange(10, [1, 5, 10, 25]))

"""
8/14/17
Giving an amount of change and a list of available denominations, coins, find the minimum
number of coins required to make c. makeChange is the optimized version of 
makeChange1, my original solution
"""
def makeChange(change, coins):

	memo=[0]+[1000] * (change)
	
	for c in coins:
	    for amount in range(c, change+1):
	        memo[amount]= min(memo[amount-c]+1, memo[amount])
	return memo[-1]

#print(makeChange(25, [1, 2, 5, 10]))


def makeChange1(change, coins):

	memo = [0] + [1000] * (change)
	for amount in range(change+1):
		for c in coins:
			if c <= amount and memo[amount-c] +1 < memo[amount]:
				memo[amount]= memo[amount-c]+1
	return memo[-1]

#print(makeChange1(25, [1, 2, 5, 10]))

"""
8/4/17
Buy and sell one share of stock, given the array of prices. Cannot 
short stock, (have to buy before selling). Return the max profit possible. 
"""

# Brute force, use two nested loops, find max from every possible transaction.
def maxProfit(prices):
	maxProfit =0
	for i in range(len(prices)):
		for j in range(i+1, len(prices)):
			maxProfit = max(maxProfit, prices[j]-prices[i])
	return maxProfit

print("brute force "+str( maxProfit([20, 1, 9, 2, 10])))
#One pass approach

def maxProfit1(prices):
	maxProfit=0
	lowestSoFar=100
	highestSoFar = 0
	for i in range(len(prices)):
		if prices[i] < lowestSoFar:
			lowestSoFar=prices[i]
		maxProfit= max(maxProfit, prices[i]-lowestSoFar)
	return maxProfit	

#print(maxProfit1([20, 1, 9, 2, 10]))


