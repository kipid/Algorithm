class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        listN = list()
        for i in range(1,n+1):
            listN.append(i)
        def facto(i: int) -> int:
            if i == 1:
                return 1
            return i * facto(i-1)
        factoList = [1]
        for i in range(1,n):
            factoList.append(i * factoList[i-1])
        res = ""
        while len(listN) > 0:
            firstIndex = k // factoList[n-1]
            # print(f"{k = }")
            res += str(listN[firstIndex])
            del listN[firstIndex]
            k = k % factoList[n-1]
            n -= 1
        return res