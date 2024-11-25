class Solution:

    def solution(self, nums):

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low+high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
x = Solution()
print(x.solution([5,6,7,1,2,3,4]))