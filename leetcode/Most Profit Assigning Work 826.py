

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:

        map_p = defaultdict(int)

        total = 0

        for (
            diff,
            prof,
        ) in zip(difficulty, profit):

            map_p[diff] = max(map_p[diff], prof)
        diff_all = sorted(map_p.keys())
        diff_max = [diff_all[0]]

        comp = sorted(zip(difficulty,profit))

        print(comp)
        comp.sort()
        print(comp)

        for i in range(1, len(diff_all)):
            before = diff_max[-1]
            curr = diff_all[i]
            if map_p[curr] > map_p[before]:
                diff_max.append(curr)

        # print(map_p)
        # print(diff_all)
        # print(diff_max)

        work_map = Counter(worker)
        for work in work_map:

            index = bisect_right(diff_max, work)
            if index != 0:
                total += map_p[diff_max[index - 1]] * work_map[work]
            # print(f"{work = } {index = } {total = }")
        return total


print(
    Solution().maxProfitAssignment(
        difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]
    )
)
print(
    Solution().maxProfitAssignment(
        difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]
    )
)


"""
826. Most Profit Assigning Work
Medium
Topics
Companies
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
 

Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 10**5
"""


'''
better solution
- create sort difficult and profit
- sort workers
- go through sorted workers
- each worked go up the difficcult ladder keeping track of max profit

class Solution:
    def maxProfitAssignment(self, d: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(d, profit))
        worker.sort()

        ans = j = maxp = 0

        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                maxp = max(maxp, jobs[j][1])
                j+=1
            ans += maxp
        return ans
'''

