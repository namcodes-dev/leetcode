def twoSum(nums, target):

    d = {}

    for i, j in enumerate(nums):
        diff = target - j
        if diff in d:
            return [i, d[diff]]
        d[j] = i
    
print(twoSum([2,7,1], 9))