#not in place solution, but easy to understand
def rotateImage(a):

    n=len(a)
    result = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j]= a[n-1-j][i]
    return result
    
    
def rotateImage(a):
    res = [[0] * len(a) for i in range(len(a))];
    for i in range(len(a)):
       for j in range(len(a[:])):
           res[i][j] = a[len(a[:])-j-1][len(a[:])-i-1];
    return res[::-1]

#reverse the lists first, then perform swaps
def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

    
    #short list comprehension same idea as above
def rotateImage(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]
