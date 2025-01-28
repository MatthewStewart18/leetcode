from typing import List
class Solution:

    def hasDuplicate(self,nums: List [int]) -> bool:
        my_set = set(nums)
        return len(my_set) < len(nums)

solution = Solution()
nums = [1,2,3,4]
print(f"Duplicate = {solution.hasDuplicate(nums)}")
