class Solution:
    def shoppingOffers(self, price, special, needs):
        
        def noSpecial(needs, price):
            sum = 0
            for n, p in zip(needs, price):
                sum += n*p
            return sum
        
        def updateNeeds(needs, offer):
            updated_needs = []
            for n, s in zip(needs, offer):
                updated_needs.append(n-s)
            return updated_needs
        
        def lowestPrice(i, needs):
            cur_min = noSpecial(needs, price)
            if i == len(special):
                return cur_min
            offer = special[i]
            for j in range(len(needs)):
                if offer[j] > needs[j]:
                    return lowestPrice(i + 1, needs) #move on to next special
            
            #update what we need
            updated_needs = updateNeeds(needs, offer)
            
            #price paid if offer used, recursive call to updated_needs
            buy_price = offer[-1] + lowestPrice(i, updated_needs) 
            
            #price paid if offer not used, recursive call to original needs
            no_buy_price = lowestPrice(i + 1, needs)
            
            return min(buy_price, no_buy_price)
        
        if needs:
            return lowestPrice(0, needs)
        else:
            return 0
        
