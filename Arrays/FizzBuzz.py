class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sol=[None]*(n)      #create an appropriately size array to hold the result
        for i in range(1, n+1):      
            if(i%15==0):             #beware of masking, check this case first!
                sol[i-1]="FizzBuzz"
            elif(i%5==0):
                sol[i-1]="Buzz"
            elif(i%3==0):
                sol[i-1]="Fizz"
            else:
                sol[i-1]=str(i)
        return sol
