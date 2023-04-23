'''
Max Heap:
Time: O(n * logn) -- n_element * max
'''
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]  # smallest neg num == largest pos num
        heapq.heapify(stones)  # python only has min heap

        while len(stones) > 1:  # at least 2 nums
            first = heapq.heappop(stones)  # smallest num1
            second = heapq.heappop(stones)  # smallest num2
            if second > first:  # second >= first (always)
                heapq.heappush(stones, first - second)  # neg

        stones.append(0)  # edge case: len(stones) == 0
        return abs(stones[0])  # neg

