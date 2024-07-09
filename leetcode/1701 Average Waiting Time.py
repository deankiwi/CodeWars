from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = 1
        waited = 0
        for time, wait in customers:
            if time >= curr:
                curr = time + wait
                waited += wait
            else:
                # curr is greater than time arrived therefor they must wait
                waited += wait + curr - time
                curr += wait

        return waited / len(customers)

