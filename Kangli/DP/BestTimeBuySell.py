class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice=sys.maxint
        maxProfit=0
        for i in range(0, len(prices)):
            if (prices[i]<minPrice):
                minPrice=prices[i]
            elif(prices[i]-minPrice>maxProfit):
                maxProfit=prices[i]-minPrice
        return maxProfit
        
