'''
DP:
    loop i - backward:
        loop j - forward:

    Time: O(n^2)
    Space: O(n)
--------------------------
Binary search + greedy:
    if num > max(LIS): LIS.append(num)
    else: min(values > num) = num  # --> append as much value as possible

    Time: O(n logn)
    Space: O(n)
'''

class Solution:
    # DP
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, 0, -1):
            for j in range(i, len(nums)-1):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return LIS
    
    # Greedy + Binary search
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [nums[0]]

        for num in nums[1:]:
            if num > LIS[-1]: 
                LIS.append(num)
                continue

            l, r = 0, len(LIS) - 1
            while l < r:  # if l == r: break
                m = (l + r) // 2

                if num > LIS[m]:
                    l = m + 1
                else:
                    r = m
            LIS[l] = num

        return len(LIS)