class Solution(object):
    def topKFrequent(self, words, k):
        d, res = {}, []
        for w in words:
            d[w] = 1 if w not in d else d[w]+1
        items = list(d.items())
        items.sort(key=lambda item:(-item[1], item[0]))
        return [item[0] for item in items[0:k]]
        
