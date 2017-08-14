"""
solutions to problems in EPI
"""

"""
8/14/17
Find the number of ways to make change
"""


"""
8/14/17
Giving an amount of change and a list of available denominations coins, find the minimum
number of coins required to make c.
"""
def makeChange(change, coins):

	memo=[0]+[1000] * (change)
	
	for c in coins:
	    for amount in range(c, change+1):
	        memo[amount]= min(memo[amount-c]+1, memo[amount])
	return memo[-1]

print(makeChange(25, [1, 2, 5, 10]))


def makeChange1(change, coins):

	memo = [0] + [1000] * (change)
	for amount in range(change+1):
		for c in coins:
			if c <= amount and memo[amount-c] +1 < memo[amount]:
				memo[amount]= memo[amount-c]+1
	return memo[-1]

print(makeChange1(25, [1, 2, 5, 10]))
	
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

print(maxProfit1([20, 1, 9, 2, 10]))


