class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        a = a[::-1]
        b = b[::-1]
        minLength = min(len(a), len(b))
        maxLength = max(len(a), len(b))
        maxStr = a if len(a) > len(b) else b
        c = ""
        for i in range(minLength):
            if carry == "1" and a[i] == "1" and b[i] == "1":
                c += "1"
                carry = "1"
            elif carry == "0" and a[i] == "1" and b[i] == "1":
                c += "0"
                carry = "1"
            elif carry == "1" and a[i] == "1" and b[i] == "0":
                c += "0"
                carry = "1"
            elif carry == "1" and a[i] == "0" and b[i] == "1":
                c += "0"
                carry = "1"
            elif carry == "0" and a[i] == "1" and b[i] == "0":
                c += "1"
                carry = "0"
            elif carry == "0" and a[i] == "0" and b[i] == "1":
                c += "1"
                carry = "0"
            elif carry == "1" and a[i] == "0" and b[i] == "0":
                c += "1"
                carry = "0"
            elif carry == "0" and a[i] == "0" and b[i] == "0":
                c += "0"
                carry = "0"
            # print(f"{c = }, {carry = }")
        for i in range(minLength, maxLength):
            if carry == "1" and maxStr[i] == "1":
                carry = "1"
                c += "0"
            elif carry == "1" and maxStr[i] == "0":
                carry = "0"
                c += "1"
            elif carry == "0" and maxStr[i] == "1":
                carry = "0"
                c += "1"
            elif carry == "0" and maxStr[i] == "0":
                carry = "0"
                c += "0"
            # print(f"{c = }, {carry = }")
        if carry == "1":
            c += "1"
        return c[::-1]