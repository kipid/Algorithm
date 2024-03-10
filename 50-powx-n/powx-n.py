class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        def powPositive(x: float, n: int) -> float:
            if n == 1:
                return x
            elif n % 2 == 0:
                return powPositive(x*x, n // 2)
            else:
                return x * powPositive(x*x, n // 2)

        if n < 0:
            return 1.0 / powPositive(x, -n)
        return powPositive(x, n)