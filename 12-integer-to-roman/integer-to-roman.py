class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        s += "M" * (num // 1000)
        num = num % 1000
        s += "CM" * (num // 900)
        num = num % 900
        s += "D" * (num // 500)
        num = num % 500
        s += "CD" * (num // 400)
        num = num % 400
        s += "C" * (num // 100)
        num = num % 100
        s += "XC" * (num // 90)
        num = num % 90
        s += "L" * (num // 50)
        num = num % 50
        s += "XL" * (num // 40)
        num = num % 40
        s += "X" *(num // 10)
        num = num % 10
        s += "IX" * (num // 9)
        num = num % 9
        s += "V" * (num // 5)
        num = num % 5
        s += "IV" * (num // 4)
        num = num % 4
        s += "I" * num
        return s