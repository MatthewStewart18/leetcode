from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        # pairs = dict.items()
        # sorted_pairs = sorted(pairs, key=lambda item: item[1], reverse=True)
        # top_k_pairs = sorted_pairs[:k]
        # top_k_keys = [key for key,value in top_k_pairs]

        # We can simply the above code into a single line list comprehension.

        top_two_keys = [key for key, value in sorted(dict.items(), key = lambda item: item[1], reverse=True)[:k]]

        return top_two_keys

solution = Solution()
nums = [1,2,2,3,3,3]
k = 2
print(solution.topKFrequent(nums, k))