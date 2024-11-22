class Solution:
    def longestSeq(self, nums):

        numset = set(nums)
        longest_streak = 0

        for n in numset:
            if (n-1) not in numset:
                curr_streak = 1

                while (n+curr_streak) in numset:
                    curr_streak += 1
                
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak

x = Solution()
print(x.longestSeq([100,4,200,1,3,2]))