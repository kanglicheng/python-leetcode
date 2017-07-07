
from collections import OrderedDict
def firstNotRepeatingCharacter(s):

    d= OrderedDict()
    for c in s:
        d[c] = 1 if c not in d else d[c]+1
    
    for k in d:
        if d[k] ==1:
            return k
    return '_'
