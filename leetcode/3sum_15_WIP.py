from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = defaultdict(int)
        output = []
        for num in nums:
            seen[num] += 1
        unique = list(seen)
        print(unique)
        for i in range(len(unique) - 1):
            if seen[unique[i]] >= 2:

                start = 0
            else:
                start = 1
            for j in range(i + start, len(unique) -1):
                print(f"{i , j = }")
                target = -unique[i] - unique[j]
                print(f"{target, unique[i], unique[j], unique[j+1:] = }")
                if target in unique[j + 1 :]:
                    output.append([unique[i], unique[j], target])
        if seen[unique[-1]] >= 2:
            target = -2 * unique[-1]
            if target in unique[:-1]:
                output.append([target, unique[-1], unique[-1]])
        if seen[0] >= 3:
            output.append([0, 0, 0])

        # we need to consider the last one having a count twice
        # and 0 3 times

        return output


print(Solution().threeSum([-2, 0, 1, 1, 2]), "= \n[[-2,0,2],[-2,1,1]]\n")
# print(Solution().threeSum([1,1,-2]), "= \n[1,1,-2]\n")
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), "= \n[[-1,-1,2],[-1,0,1]]")
# print(Solution().threeSum([-1, 0, 1, 2,-1,  8, -4, -4]), "= \n")
# print(
#     Solution().threeSum([-1, 0, 1, 2, 0, 0, 0, 8, -4, -4]), "= \n"
# )


"""
15. 3Sum
Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


'''
possible solutions

this one uses sets and tuple to store unique vectors
'res.add(tuple(sorted([n[i],n[j],target])))'

def threeSum(self, nums: List[int]) -> List[List[int]]:

	res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res
'''

