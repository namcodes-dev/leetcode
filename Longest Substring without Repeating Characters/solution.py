class Solution:
    def solution(self, s):
        charSet = set()
        l = 0
        longest = 0
        n = len(s)

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            w = r - l + 1
            longest = max(w, longest)
        return longest

x = Solution()
print(x.solution("abcabcbb"))