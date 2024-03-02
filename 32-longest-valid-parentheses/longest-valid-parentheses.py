class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1]
        ans = 0

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans