"""
solutions to problems in EPI
"""

"""
8/14/17
Find the number of ways to make change, given an amount change and 
an array of denominations, coins.
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""
# Dynamic Programming Python implementation of Coin Change problem
def count(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
 
    return table[n][m-1]


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


