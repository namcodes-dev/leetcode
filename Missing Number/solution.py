from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        s = (n*(n+1))//2
        res = s - sum(nums)
        return res