import re

class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(k):
            curVal = 0
            digit = 0
            sign = 1
            while k < len(s):
                if s[k] == " ":
                    k += 1
                    continue
                elif s[k] == "(":
                    subVal, k = evaluate(k+1)
                    curVal += sign * subVal
                elif s[k] == ")":
                    curVal += sign*digit
                    return curVal, k
                elif s[k] == "-":
                    curVal += sign * digit
                    digit = 0
                    sign = -1
                elif s[k] == "+":
                    curVal += sign * digit
                    digit = 0
                    sign = 1
                elif s[k].isdigit():
                    digit = digit * 10 + int(s[k])
                k += 1
            return curVal + sign * digit
        return evaluate(0)