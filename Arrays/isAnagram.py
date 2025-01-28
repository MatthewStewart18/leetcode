class Solution:

# Sorting into alphabetical order has a time complexity of O(n log n) - where n
# is the length of the string, frequency count approach belows provides a more
# efficient O(n) solution

#     def sortedString(self, string: str):
#         return ''.join(sorted(string))

#     def isAnagram(self, s: str, t: str) -> bool:
#         s_sort = self.sortedString(s)
#         t_sort = self.sortedString(t)

#         return s_sort == t_sort

# solution = Solution()
# s = "racecar"
# t = "carrace"
# print(solution.isAnagram(s,t))

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1

        return all(value == 0 for value in freq.values())

solution = Solution()
print(solution.isAnagram("ratt", "carr")) # Expected False