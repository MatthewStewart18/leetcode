from typing import List
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     output = []
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 output.append(i)
    #                 output.append(j)
    #                 return output

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            desired = target - num
            if desired in seen:
                return [seen[desired], i]
            seen[num] = i

solution = Solution()
nums = [3,4,5,6]
target = 7
print(solution.twoSum(nums, target)) # Expected [0,1]
