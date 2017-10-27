Keeping a record of thoughts behind solving certain problems

10/27/17
219: Contains Duplicate II: Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
Thoughts:
Use a dictionary to store each integer and its index in nums as key, value pairs. 
If a value is already in the dictionary, check whether index difference <= k. 

Implementation: did not pass on first 2 tries, failed for [1, 0, 1, 1, ], 1 (true got false). Need to update
index if value already in dictionary but i - d[n] > k. 

49: Group Anagrams: Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Thoughts: Using a dictionary (hash), insert each sorted string into the dictionary as keys, using the original string as the value. Need the values to be an array, so initialize the value of each key as [] and add the original string directly to [] each time. Could also use defaultdict (python specific). 
