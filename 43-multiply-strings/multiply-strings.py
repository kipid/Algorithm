class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if len(num1) > len(num2):
        #     num1, num2 = num2, num1
        res = [0 for _ in range(len(num1) + len(num2))]
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                multi = int(n1) * int(n2)
                res[i + j] += multi
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        k = len(num1) + len(num2) - 1
        for i in range(k):
            res[i+1] += res[i] // 10
            res[i] = res[i] % 10
        ans = ""
        while k > 0 and res[k] == 0:
            k -= 1
        while k >= 0:
            ans += str(res[k])
            k -= 1
        return ans