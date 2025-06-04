# Last updated: 04/06/2025, 12:42:08
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while (left < right):
            currentsum = numbers[left] + numbers[right]
            if (currentsum > target):
                right -= 1
            elif (currentsum < target):
                left += 1
            else:
                return [left +1, right+1]
        return [left + 1, right + 1]
        