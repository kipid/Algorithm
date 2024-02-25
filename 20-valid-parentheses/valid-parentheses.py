class Solution:
    def isValid(self, s: str) -> bool:
        brakets = []
        for l in s:
            if l == "(" or l == "{" or l == "[":
                brakets.append(l)
            elif l == ")":
                if len(brakets) == 0 or "(" != brakets.pop():
                    return False
            elif l == "}":
                if len(brakets) == 0 or "{" != brakets.pop():
                    return False
            elif l == "]":
                if len(brakets) == 0 or "[" != brakets.pop():
                    return False
        if len(brakets) > 0:
            return False
        return True

