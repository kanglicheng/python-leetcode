def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    d={}
    res=[]
    for l in lettersGuessed:
        d[l]=1 if l not in d else d[l]+1
        
    for letter in secretWord:
        if letter in d:
            res.append(letter)
        else:
            res.append('_')
    return "".join(str(x) for x in res)

