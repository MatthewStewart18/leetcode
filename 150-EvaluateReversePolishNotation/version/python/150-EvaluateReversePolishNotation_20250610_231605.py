# Last updated: 10/06/2025, 23:16:05
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        mapping = ['+', '-', '*', '/']

        for token in tokens:
            if token in mapping:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:
                    result = int(left / right)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]

        