import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.sub(r"\*+", "*", p)
        
        def match(s: str, sIndex: int, p: str, pIndex: int) -> bool:
            if sIndex >= len(s) and pIndex >= len(p):
                return True
            elif sIndex < len(s) and pIndex >= len(p):
                return False
            elif sIndex >= len(s) and pIndex < len(p):
                if pIndex == len(p) - 1 and p[pIndex] == "*":
                    return True
                else:
                    return False
            else:
                if p[pIndex] == "?":
                    return match(s, sIndex+1, p, pIndex+1)
                elif p[pIndex] == "*":
                    k = 1
                    offset = -1
                    matched = True
                    if pIndex+k == len(p):
                        return True
                    while pIndex+k < len(p) and sIndex+offset+k < len(s) and p[pIndex+k] != "?" and p[pIndex+k] != "*":
                        matched = matched and s[sIndex+offset+k] == p[pIndex+k]
                        # print(f"{matched = }, {s[sIndex+offset+k] = }, {p[pIndex+k] = }")
                        if matched:
                            k += 1
                        else:
                            matched = True
                            k = 1
                            offset += 1
                    return (matched and match(s, sIndex+offset+k, p, pIndex+k)) or match(s, sIndex+1, p, pIndex)
                else:
                    k = 0
                    matched = True
                    while pIndex+k < len(p) and sIndex+k < len(s) and p[pIndex+k] != "?" and p[pIndex+k] != "*":
                        matched = matched and (s[sIndex+k] == p[pIndex+k])
                        k += 1
                    return matched and match(s, sIndex+k, p, pIndex+k)
        
        # pRIndex, sRIndex = len(pattern)-1, len(s)-1
        # matched = True
        # while pRIndex >= 0 and sRIndex >= 0 and pattern[pRIndex] != "?" and pattern[pRIndex] != "*":
        #     matched = matched and pattern[pRIndex] == s[sRIndex]
        #     if matched:
        #         pRIndex -= 1
        #         sRIndex -= 1
        #     else:
        #         break
        # if not matched:
        #     return False
        return match(s[::-1], 0, pattern[::-1], 0)
