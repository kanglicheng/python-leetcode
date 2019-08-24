"""
Partition an array for quicksort, aka Dutch national flag problem.
Write a program that takes an array A and an index i into A, and rearranges 
the elements such that all elements less than A[i] appear first, followed by
elements equal to the pivot followed by elements greater than the pivot.

Example: A=[-3, 0, -1, 1, 1, 2, 4, 3, 5], i = 4, A is already partitioned correctly.
12/27/17
"""

# We can create 3 new lists/arrays, one with all elements < p, another all
#elements = p, and the third all elements > p. O(n) time but O(n) space also.

def partition_1(arr, i):
	p = arr[i]
	a1, a2, a3, = [], [], []
	for n in arr:
		if n < p:
			a1.append(n)
		elif n == p:
			a2.append(n)
		else:
			a3.append(n)
	return a1 + a2 + a3

#print partition_1([4, 5, 2, -1, 0, 2, 1], 2)
#got [-1, 0, 1, 2, 2, 4, 5], correct answer

#first pass groups elements < p, second pass groups elements >p
# O(1) space and O(n) time
def partition_opt(arr, i):
	p = arr[i]
	smaller = 0
	for i in range(len(arr)):
		if arr[i] < p:
			arr[i], arr[smaller] = arr[smaller], arr[i]
			smaller += 1
	larger = len(arr)-1
	for i in reversed(range(len(arr))):
		if arr[i] < p:
			break
		elif arr[i] > p:
			arr[i], arr[larger] = arr[larger], arr[i]
			larger -= 1
	return arr

print partition_opt([4, 5, 2, -1, 0, 2, 1], 2)

"""
Write a program which takes an array of digits representing a number N
and update the array to represent N+1.
"""
<<<<<<< HEAD


def knapsack(items, weights, W):
	
=======
>>>>>>> 7488e4d602261a8615cebaf51ea6ebaac4ccb207

