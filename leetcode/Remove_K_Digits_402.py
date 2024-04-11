

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        start = ""
        completions = 0

        length = len(num)

        if length == k:
            return "0"

        while k > 0:

            if completions + k >= length:
                completions = length
                break

            check_numbers = num[completions : k + completions + 1]

            # print(f"{num=} {k=} {completions=}  {check_numbers=}")
            smallest_num = min(check_numbers)

            index_of_smallest = check_numbers.index(smallest_num)
            start += check_numbers[index_of_smallest]

            k -= index_of_smallest

            completions += 1 + index_of_smallest
            while (
                len(check_numbers) - 1 > index_of_smallest
                and check_numbers[index_of_smallest + 1] == smallest_num
            ):
                completions += 1
                start += smallest_num
                if completions + k >= length:
                    completions = length
                    break

            # print(f"{index_of_smallest=} {start=}")

        # print()
        # print(f"{completions=}")
        num = start + num[completions:]
        while num[0] == "0" and len(num) > 1:
            num = num[1:]
        return num


print(Solution().removeKdigits(num="12121", k=2), "= 111")
print(Solution().removeKdigits(num="121219", k=2), "= 1119")
print(Solution().removeKdigits(num="1432219", k=3), "= 1219")
print(Solution().removeKdigits(num="10200", k=1), "= 200")
print(Solution().removeKdigits(num="101", k=1), "= 1")
print(Solution().removeKdigits(num="1110", k=3), "= 0")
print(Solution().removeKdigits(num="10", k=2), "= 0")
print(Solution().removeKdigits(num="112", k=1), "= 11")


'''
Could not get it in the correct time complexity, All you needed to do was start at the front and only add numbers to the back if you k > 0 and it is less than the last number


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            
            if st or n is not '0': # prevent leading zeros
                st.append(n)
                
        if k: # not fully spent
			st = st[0:-k]
            
        return ''.join(st) or '0'
'''

