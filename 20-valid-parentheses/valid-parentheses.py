class Solution:
    def isValid(self, s: str) -> bool:
        brakets = []
        l = s[0]
        if not (l == "(" or l == "{" or l == "["):
            return False
        else:
            brakets.append(l)
        for l in s[1:]:
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

