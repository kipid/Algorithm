class Solution:
    def reverse(self, x: int) -> int:
        isMinus = (x < 0)
        if isMinus:
            x = -x
        res = x % 10
        print(f"res: {res}")
        while (x := x // 10) > 0:
            print(f"res: {res}, x: {x}")
            res = 10 * res + x % 10
        if isMinus:
            res = -res
        return res

sol = Solution()
print(sol.reverse(123))

