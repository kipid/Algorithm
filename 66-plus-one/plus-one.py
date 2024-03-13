class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        done = False
        for i in range(len(digits)-1, 0, -1):
            if digits[i] >= 10:
                digits[i-1] += digits[i] // 10
                digits[i] %= 10
            else:
                done = True
                break
        if not done and digits[0] >= 10:
            digits.insert(0, digits[0] // 10)
            digits[1] %= 10
        return digits