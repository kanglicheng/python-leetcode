
#my first solution
def firstDuplicate(a):
    d= {}
    for s in a:
        if s not in d:
            d[s]=1
        else:
            return s
    return -1

def firstDuplicate(a):
    mySet=set()
    for el in a:
        if el in mySet:
            return el
        mySet.add(el)
    return -1

def firstDuplicate(a):
    for i in a:
        a[abs(i)-1] *= -1
        if a[abs(i)-1] > 0:
            return abs(i)
    return -1
