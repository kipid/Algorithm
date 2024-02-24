class Solution:
    def subIntToRoman(self, num: int, digit: int, s10: str, s5: str, s1:str) -> (str, int):
        s = ""
        s += s10 * (num // (digit*10))
        resi = num % (digit*10)
        if resi >= 9*digit:
            s += s1 + s10
            resi %= 9*digit
        elif resi >= 5*digit:
            resi %= 5*digit
            s += s5 + s1 * (resi // digit)
            resi %= digit
        elif resi >= 4*digit:
            resi %= 4*digit
            s += s1 + s5
        else:
            s += s1 * (resi // digit)
            resi %= digit
        return (s, resi)

    def intToRoman(self, num: int) -> str:
        (s0, num) = self.subIntToRoman(num, 100, "M", "D", "C")
        (s1, num) = self.subIntToRoman(num, 10, "C", "L", "X")
        (s2, num) = self.subIntToRoman(num, 1, "X", "V", "I")
        return s0 + s1 + s2