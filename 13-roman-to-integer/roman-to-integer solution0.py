class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {
            "I":1, "VI":4, "V":5, "XI":9,
            "X":10, "LX":40, "L":50, "CX":90,
            "C":100, "DC":400, "D":500, "MC":900, "M":1000
        }
        i = 0
        sum = 0
        revS = s[::-1]
        while i < len(revS) - 1:
            if revS[i:i+2] in dict_:
                sum += dict_[revS[i:i+2]]
                i += 2
            elif revS[i:i+1] in dict_:
                sum += dict_[revS[i:i+1]]
                i += 1
        if i < len(revS):
            sum += dict_[revS[i:i+1]]
        return sum