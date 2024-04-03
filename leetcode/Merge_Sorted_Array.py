

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1, nums2)

        length = len(nums1)

        for i in range(length - 1, -1, -1):
            # print(i, n, m, nums1)
            if n == 0: break
            if m == 0: break
            if nums2[n-1] >= nums1[m-1]:
                nums1[i] = nums2[n-1]
                n -= 1
            else:
                nums1[i] = nums1[m-1]
                m-=1
        for i in range(n):
            nums1[i] = nums2[i]



test = Solution()

testArr1 = [1, 2, 3, 0, 0, 0]
test.merge(testArr1, 3, [2, 5, 6], 3)
print(testArr1)

testArr1 = [6, 6, 6, 0, 0, 0]
test.merge(testArr1, 3, [1, 1, 1], 3)
print(testArr1)

testArr1 = [1,2,3]
test.merge(testArr1,3,[],0)
print(testArr1)

testArr1 = [0]
test.merge(testArr1,3,[1],0)
print(testArr1)



class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1, nums2)

        length = len(nums1)

        for i in range(length - 1, -1, -1):
            # print(i, n, m, nums1)
            if n == 0: break
            if m == 0: break
            if nums2[n-1] >= nums1[m-1]:
                nums1[i] = nums2[n-1]
                n -= 1
            else:
                nums1[i] = nums1[m-1]
                m-=1
        for i in range(n):
            nums1[i] = nums2[i]



test = Solution()

testArr1 = [1, 2, 3, 0, 0, 0]
test.merge(testArr1, 3, [2, 5, 6], 3)
print(testArr1)

testArr1 = [6, 6, 6, 0, 0, 0]
test.merge(testArr1, 3, [1, 1, 1], 3)
print(testArr1)

testArr1 = [1,2,3]
test.merge(testArr1,3,[],0)
print(testArr1)

testArr1 = [0]
test.merge(testArr1,3,[1],0)
print(testArr1)

