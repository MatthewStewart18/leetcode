# Last updated: 08/06/2025, 02:07:08
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                continue
        return not stack
        