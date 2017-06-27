"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

https://leetcode.com/static/images/problemset/keyboard.png
![alt text](https://leetcode.com/static/images/problemset/keyboard.png)
American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
#my brute force solution, but accepted.
class Solution(object):
    def findWords(self,  words):
    
        d1={x:1 for x in ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')}
        d2={x:1 for x in ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')}
        d3={x:1 for x in ('z', 'x', 'c', 'v', 'b', 'n', 'm')}
        res=[]
        for word in words:
            word1=word.lower()
            b, b1, b2 = True, True, True
            for w in word1:
                if w not in d1:
                    b=False
            for w in word1:
                if w not in d2:
                    b1=False
            for w in word1:
                if w not in d3:
                    b2=False
            if b or b1 or b2:
                res.append(word)
        return res
