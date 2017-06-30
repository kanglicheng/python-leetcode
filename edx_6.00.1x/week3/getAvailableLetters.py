import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    d = {}
    res=[]
    lowerCaseLetters = string.ascii_lowercase
    for l in lettersGuessed:
        d[l]=1 if l not in d else d[l]+1
    for c in lowerCaseLetters:
        if c not in d:
            res.append(c)
    return "".join(x for x in res)
