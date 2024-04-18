class Solution:
    def calculate(self, s: str) -> int:
        curr, res, sign = 0, 0, 1
        stack = [] # (res, sign)

        for c in s:
            # print("----")
            # print(c)
            if c == ' ':
                continue
            if c == "(":
                stack.append((res, sign))
                curr, res, sign = 0, 0, 1
            elif c == ")":
                res += curr * sign
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign * res
                curr, sign = 0, 1
            elif c in ["+", "-"]:
                res += curr * sign
                sign = 1 if c == "+" else -1
                curr = 0
            else:
                curr = curr * 10 + int(c)
            # print(curr, res, sign)
        res += curr * sign
        return res