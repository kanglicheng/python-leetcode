### How I Practice ###
Keeping a record of thoughts behind solving certain problems

1/4/18 Making some catch-up edits.
**189: Rotate Array-**
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Hint: Related problem: Reverse Words in a String II. An "easy" problem but with a low acceptance rate, only 25%, wonder why.

*Thoughts: Really struggled with the constraint of doing it in place. So tried solving it with extra space first. 
Just append the elements in the correct positions in the new results array. But coming up with the correct positions requires thinking about two conditions. As we iterate through the input nums, we simply put put nums[i] at res[i+k] if i+k is a valid index (i + k < len(nums) ). But if i + k exceeds len(nums), what to do? Also k can be any positive number, meaning it could be several times len(nums). I worked out a few examples arr = [1, 2, 3], k=1, k= 2, k = 5 etc. Then I found the pattern that the correct position corresponds to (i + k) % len(nums), for any i and k. This is also correct mathematically because we are really looking for the number (i + k) that "wraps around" len(nums), which is exactly what modulo arithmetic can be used for.

I later looked up an in-place solution that pops the last item of the array and inserts it to the beginning, repeating for k % len(nums) times. 
* 
[Submission](https://github.com/kanglicheng/python-leetcode/blob/mySolutions/Kangli/Arrays/rotateArray.py)


**387: First Unique Character in a String-**
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

*Thoughts: Straightforward use of a hash to store the counts of each letter in the string. Then iterate the string again from the beginning and return the first letter with count of 1.*
[Submission](https://github.com/kanglicheng/python-leetcode/blob/mySolutions/Kangli/Strings/firstUniqueChar.py)

**443: String Compression-** Given an array of characters, compress it in-place. The length after compression must always be smaller than or equal to the original array. Every element of the array should be a character (not int) of length 1. After you are done modifying the input array in-place, return the new length of the array.

Example: 
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

*Thoughts: Easy if not doing it in place. I made an extra array, added the character and added its count
if count > 1. Return the length of new array at the end. *
[Submission](https://github.com/kanglicheng/python-leetcode/blob/mySolutions/Kangli/Strings/stringCompression.py)

10/27/17

**219: Contains Duplicate II-** Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
*Thoughts:
Use a dictionary to store each integer and its index in nums as key, value pairs. 
If a value is already in the dictionary, check whether index difference <= k. *

Implementation: did not pass on first 2 tries, failed for [1, 0, 1, 1, ], 1 (true got false). Need to update
index if value already in dictionary but i - d[n] > k.
[Submission](https://github.com/kanglicheng/python-leetcode/blob/mySolutions/Kangli/Hash%20Table/containsDuplicate_II.py)

**49: Group Anagrams-** Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
*Thoughts: Using a dictionary (hash), insert each sorted string into the dictionary as keys, using the original string as the value. Need the values to be an array, so initialize the value of each key as [] and add the original string directly to [] each time. Could also use defaultdict (python specific). *
[Submission](https://github.com/kanglicheng/python-leetcode/blob/mySolutions/Kangli/Hash%20Table/group_anagrams.py)

11/7/17

**206: Reverse Linked List**
Have access to the head of the linked list. Want to reverse the pointers and make the original head point to null (end of list). 
1) Recursively, we begin with the base case of returning head if head is null or head.next is null.
Then we declare a tailNode to be head.next and have the tailNode point to head. (tailNode.next=head). This process continues until we reach the end of the list, which is the base case. Finally make the original head point to null. 
2) Iteratively, reverse the list one node at a time starting at the head. Need 3 pointers to traverse the list. Have a temp be current.next, then make current.next point to the last node in the already reversed part of the list. Then update the alreadyReversed pointer to current, and finally update current to temp (current.next). When current is null, the loop exits and return alreadyReversed, now the head of the reversed list. 
https://youtu.be/j6dEFsH_Aqg 
