
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        links = {}
        for course, pre in prerequisites:
            print(f'{course = }, {pre = }')
            if pre not in links:
                links[course] = pre
            seen = set([course])

            curr = pre
            while True:
                if curr in seen:
                    return False
                if curr not in links:
                    break
                else:
                    curr = links[curr]
        print(links)

        return True


# print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution().canFinish(3, [[1,0],[1,2],[0,1]]) , ' == False')


"""
207. Course Schedule
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

