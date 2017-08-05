"""

"""


"""
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

