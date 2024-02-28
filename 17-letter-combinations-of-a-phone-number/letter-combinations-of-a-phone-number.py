class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_ = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
        res = []
        if len(digits) > 0:
            res = dict_[digits[0]]
            for c in digits[1:]:
                res1 = []
                for l1 in dict_[c]:
                    res1 += [ l + l1 for l in res ]
                res = res1
        return res