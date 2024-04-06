
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:  

        jumps = 0
        index = 0

        endpoint = len(nums) - 1


        while index < endpoint:
            jumps += 1
            max_jump = nums[index]

    
            if index + max_jump >= endpoint:

                return jumps

            possible_jumps = [
                i + j + 1 for i, j in enumerate(nums[index + 1 : index + max_jump + 1])
            ]

            next_max_jump = max(possible_jumps)



            index += possible_jumps.index(next_max_jump) + 1


        return jumps


'''
better solution: kind of simular idea to keep track on the furthest jump and only jump there but far more simple
class Solution:
  def jump(self, nums: List[int]) -> int:
    ans = 0
    end = 0
    farthest = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
      farthest = max(farthest, i + nums[i])
      if farthest >= len(nums) - 1:
        ans += 1
        break
      if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = farthest  # Make the queue size for the next level

    return ans
'''

print(Solution().jump([1, 0]), 1)
print(Solution().jump([1, 1, 0]), 2)
print(Solution().jump([1, 1, 1, 0]), 3)
print(Solution().jump([1, 1, 1, 1, 0]), 4)
print(Solution().jump([1, 1, 1, 1, 1, 1, 5, 4, 3, 2, 1, 0]))
print(Solution().jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))
print(Solution().jump([2, 3, 1, 1, 4]), 2)
print(Solution().jump([10]))

print(
    Solution().jump(
        [
            5,
            8,
            1,
            8,
            9,
            8,
            7,
            1,
            7,
            5,
            8,
            6,
            5,
            4,
            7,
            3,
            9,
            9,
            0,
            6,
            6,
            3,
            4,
            8,
            0,
            5,
            8,
            9,
            5,
            3,
            7,
            2,
            1,
            8,
            2,
            3,
            8,
            9,
            4,
            7,
            6,
            2,
            5,
            2,
            8,
            2,
            7,
            9,
            3,
            7,
            6,
            9,
            2,
            0,
            8,
            2,
            7,
            8,
            4,
            4,
            1,
            1,
            6,
            4,
            1,
            0,
            7,
            2,
            0,
            3,
            9,
            8,
            7,
            7,
            0,
            6,
            9,
            9,
            7,
            3,
            6,
            3,
            4,
            8,
            6,
            4,
            3,
            3,
            2,
            7,
            8,
            5,
            8,
            6,
            0,
        ]
    )
)

