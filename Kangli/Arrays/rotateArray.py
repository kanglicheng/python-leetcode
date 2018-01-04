class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        res = [0 for _ in range(l)]
        for i in range(l):
            if i + k < l:
                res[i+k] = nums[i]
            elif i + k >= l:
                pos = (i + k) % l
                res[pos] = nums[i]
        nums[:] = res 

class Solution(object):
    def rotate(self, nums, k):
        n = k % len(nums)
        for i in xrange(n):
            nums.insert(0, nums.pop())


# sample 238 ms submission, from leetcode.com
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
# 我尝试了每次平移 k个位置，直到回到原来位置为止， 这个方法，如果碰到，n是k的倍数的情况 就会出现错误。


# 解决了， 如果碰到target==start 的情况，让target 和start 都加1 ，相当于略过，进行下一轮 替换， 直到counter 减到0 为止（意味着所有元素都换过一次了，结束）

        if len(nums)<=1:
            return
        if k%len(nums)==0:
            return
        n=len(nums)
        pre=nums[0]
        target=0
        start=0
        counter=n

        while (counter>0):
            target=(target+k)%n
            print "current target",target
            
            current=nums[target]
                
            nums[target]=pre
                
            if target==start:
                start+=1
                target+=1
                pre=nums[target]
                
            else:
                
                pre=current
            
            counter-=1
                

        
#         解法一 [ 时间复杂度O（n），空间复杂度O(1) ]：
# 以n - k为界，分别对数组的左右两边执行一次逆置；然后对整个数组执行逆置。

# reverse(nums, 0, n - k - 1)
# reverse(nums, n - k, n - 1)
# reverse(nums, 0, n - 1)



#         if len(nums)<=1:
#             return
#         k=k%len(nums)
       
#         for i in xrange(0,(len(nums)-k+1)/2):
#             nums[i],nums[len(nums)-k-1-i]=nums[len(nums)-k-1-i],nums[i]
#         for i in xrange(0,(k+1)/2):
#             nums[len(nums)-k+i],nums[len(nums)-1-i]=nums[len(nums)-1-i],nums[len(nums)-k+i]
        
#         for i in xrange((len(nums)+1)/2):
#             nums[i],nums[len(nums)-1-i]=nums[len(nums)-1-i],nums[i]
    
   
    
 # extra space
#         n=len(nums)
#         a=nums
#         if k>n:
#             k=k%n
#         b=[0 for i in xrange(n)]
#         for i in xrange(k):
            
#             b[i]=a[n-k+i]
#         for i in xrange(k,n):
#             b[i]=a[i-k]
#         print b
#         for i in xrange(len(nums)):
#             nums[i]=b[i]
