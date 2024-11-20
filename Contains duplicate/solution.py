from typing import List
def hasDuplicate(nums: List[int]) -> bool:
         
    return not len(set(nums)) == len(nums)

print(hasDuplicate([1,1,1,2]))