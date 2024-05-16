class Solution:
    def isHappy(self, n: int) -> bool:
        setN = set()
        setN.add(n)
        
        def next(n: int) -> int:
            nextN = 0
            while n // 10 != 0:
                nextN += (n%10) ** 2
                n = n // 10
            nextN += (n%10) ** 2
            return nextN
        
        while (n := next(n)) not in setN:
            setN.add(n)
        
        return next(n) == 1