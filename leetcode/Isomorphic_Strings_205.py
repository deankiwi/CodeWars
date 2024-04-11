
from pprint import pprint



# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         s_to_t_key = {}
#         t_to_s_key = {}

#         for i in range(len(s)):
#             if s[i] in s_to_t_key:
#                 if s_to_t_key[s[i]] != t[i]:
#                     return False
#             elif t[i] in t_to_s_key:
#                 if t_to_s_key[t[i]] != s[i]:
#                     return False
#             else:
#                 s_to_t_key[s[i]] ,t_to_s_key[t[i]] = t[i],s[i]
                
#             pprint(f'{s_to_t_key = }')
#             pprint(f'{t_to_s_key = }')

#         return True

class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        print( map1, map2)
        return False


# print(Solution().isIsomorphic("egg", "add"), "= true")
# print(Solution().isIsomorphic("foo", "bar"), "= false")
print(Solution().isIsomorphic("badc", "baba"), "= false")
print(Solution().isIsomorphic("abbba", "baaba"), "= false")

'''
cleaner solution in which they mapped over logging the index of each 

# Time Complexity : O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
'''

