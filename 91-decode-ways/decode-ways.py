import re

class Solution:
    def numDecodings(self, s: str) -> int:
        if re.search(r"00+", s):
            return 0
        # 1 => 1 (1)
        # 11 => 1 1, 11 (2)
        # 111 => 1 1 1, 1 11, 11 1 (3)
        # 1111 => 1 1 1 1, 1 1 11, 1 11 1, 11 1 1, 11 11 (5)
        # 11111 => 1 1 1 1 1, 1 1 1 11, 1 1 11 1, 1 11 1 1, 1 11 11, 11 1 1 1, 11 1 11, 11 11 1 (8)
        # 피보나치 수열.
        # 2626 => 2 6 2 6, 2 6 26, 26 2 6, 26 26 (4 = 2 * 2)
        # 2711 => 2 7 1 1, 2 7 11 (2 = 1 * 1 * 2)
        # 6보다 크면 split
        # 2보다 크면 split (6보단 작거나 같음)
        # 0이면 split (바로 앞자리랑 엮어서 counting)
        Fibonacci = [1, 1]
        for i in range(2, 101):
            Fibonacci.append(Fibonacci[-2]+Fibonacci[-1])
        # def counting(n: int) -> int:
        #     # if n == 2:
        #     #     return 2
        #     if n == 1:
        #         return 1
        #     if n == 0:
        #         return 1
        #     return counting(n-1)+counting(n-2)
        res = 1
        splitAbove6 = re.split(r"[7-9]", s)
        lastStrIndex = -1
        for i0, s0 in enumerate(splitAbove6): # 23 7 612342116 9 65
            if len(s0) > 0:
                splitAbove2 = re.split(r"[3-6]", s0)
                length = 0
                for i1, s1 in enumerate(splitAbove2): # 3 11201212210120 5 4 9 8 12011
                    if len(s1) > 0:
                        splitBy0 = re.split(r"0", s1)
                        if splitBy0[0] == "":
                            return 0 # incompatible 0
                        for i2, s2 in enumerate(splitBy0):
                            lastStrIndex += 1 + len(s2) # split 포함 indexing
                            length = len(s2) # 1 0, 112 0 121221 0 12 0 (0을 바로 전과 묶음)
                            if i2 != len(splitBy0)-1:
                                res *= Fibonacci[length-1]
                        if len(splitBy0[-1]) > 0 and splitBy0[-1][-1] != "" and lastStrIndex < len(s): # 1 0 2 ("1" or "2")
                        # no and i1 != len(splitAbove2)-1
                            if splitBy0[-1][-1] == "1":
                                length += 1
                            elif int(s[lastStrIndex]) < 7: # splitBy0[-1][-1] == "2"
                                length += 1
                        print(f"{length = }")
                        res *= Fibonacci[length]
                    else:
                        lastStrIndex += 1
                # if len(splitAbove2[-1]) > 0 and splitAbove2[-1][-1] != "" and lastStrIndex < len(s): # 23 7 612342111 9 8 65 7
                #     if splitAbove2[-1][-1] == "1":
                #         length += 1
                #     elif splitAbove2[-1][-1] == "2" and int(s[lastStrIndex]) < 7:
                #         length += 1
                # res *= counting(length - 1)
            else:
                lastStrIndex += 1
        return res