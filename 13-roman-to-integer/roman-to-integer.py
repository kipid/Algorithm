class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {
            "I":1, "V":5,
            "X":10, "L":50,
            "C":100, "D":500,
            "M":1000
        }
        sum = 0
        for i in range(len(s)-1):
            if dict_[s[i+1:i+2]] > dict_[s[i:i+1]]:
                sum -= dict_[s[i:i+1]]
            else:
                sum += dict_[s[i:i+1]]
        sum += dict_[s[len(s)-1:]]
        return sum