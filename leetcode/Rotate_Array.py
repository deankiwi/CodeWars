from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        shiftBy = k % length
        if not shiftBy:
            return

        nums[:] = nums[-shiftBy:] + nums[: length - shiftBy]


arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
print(Solution().rotate(arr, 3))
print(arr)

"""
I personally like this solution but another solution may be suitable

From Leetcoe Kooskoos
This post assumes you have already explored the reversing based solution which pretty much says:
For k=2
12345 -> 54321
54321->45321
45321->45123

So why does this work?

Let us understand the significance of k. k is nothing but a pivot point.
What this means is, in case of 12345 with k = 2, your pivot point lies at 123|45.

We want to rotate the entity along the pivot point. For simplicity let us denote either sides of pivot point as single entities as X|Y where X = 123 and Y = 45.

When we are done rotating the aggregate entity it looks something like Y|X.
Let us now understand why this tranlates to reversing the entire array. The crucial thing we will try to understand here is why irrespective of where the pivot point lies, we alwasys have to reverse the array.

The answer for this is irrespective of where you keep the pivot point the reverse always fetches the same result. Let us try to understand this. When we say reverse by default we mean mirror from the mid point.

12|34 -> 43|21

But what else is possible? Does it still fetch the same result when mirror point is changed? Let's observe

1|234 -> 432|1

Wow, why did this happen? We can understand this by adding additional padding on the lighter side and always positioning the mirror at the center. The same string can be returned as:

001|234 -> 432|100

You can alwasys balance the sides with padding resulting in the same result. So complete reverse across any pivot points fetches the same result. That is all character end up changing sides. Think about it.

Now that we have converted X|Y to Y'|X', we know in the process we ended of mirroring contents of X and Y as well.
Where Y' means Y reverse
and X' means X reverse
So in the next step we mirror them back to get the same configuration like below.

In reverse 1, X transformed this way 123 -> 321, we do not desire this transformation.
So to fix it we use:
Mirror(reverse)+Mirror(reverse) -> Original

So we reverse X and Y individually again.
So X again transforms 321 -> 123

And we get our answer 123|45 -> 45|123

Hope this was helpful. Happy learning :)


and solution by artod
def rotate(self, nums: List[int], k: int) -> None:
	L = len(nums)
	if L == k: return

	k = k%L # the case when k > L
	nums.reverse()

	for i in range(k//2):
		nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

	for i in range(k, (L+k)//2):
		nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]
"""

