class Solution:

    def sortedString(self, string: str):
        return ''.join(sorted(string))

    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = self.sortedString(s)
        print(s_sort)
        t_sort = self.sortedString(t)
        print(t_sort)

        return s_sort == t_sort

solution = Solution()
s = "racecar"
t = "carrace"
print(solution.isAnagram(s,t))

