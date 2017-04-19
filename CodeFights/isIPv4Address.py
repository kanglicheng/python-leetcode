def isIPv4Address(inputString):
    result= inputString.split('.')
    
    if(len(result) != 4):
        return False
    for s in result:
        if  (s.isdigit() == False):
            return False
        if(float(s) > 255 or float(s) < 0):
            return False
    return True
        
        
