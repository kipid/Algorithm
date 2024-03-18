class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0,1]
        minus1 = self.grayCode(n-1)
        highestBit = 1 << (n-1)
        return minus1 + [highestBit + minus1[i] for i in range(len(minus1)-1, -1, -1)]
        # [000,001,011,010
        # ,110,111,101,100]
        # [0000,0001,0011,0010
        # ,0110,0111,0101,0100
        # ,1100,1101,1111,1110
        # ,1010,1011,1001,1000]
