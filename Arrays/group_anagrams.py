from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            result[s_sorted].append(s)
        return result.values()
        

solution = Solution()
strs = ["hat", "cat", "act"]
print(solution.groupAnagrams(strs))