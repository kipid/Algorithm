class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if 4 <= n <= 12:
            # 0 1 2 3 4 5 ... n-2 n-1
            if n==4:
                return [s[0]+"."+s[1]+"."+s[2]+"."+s[3]]
            li = []
            if n==12:
                for i in range(0, n, 3):
                    if s[i]=="0" or int(s[i:i+3]) > 255:
                        return []
                    li.append(s[i:i+3])
                return [".".join(li)]
            res = []
            if s[0]=="0":
                i0MaxLength = 1
            elif int(s[0]) > 2:
                i0MaxLength = 2
            else:
                i0MaxLength = 3
            for i0 in range(1, 1+i0MaxLength): # min(n-2, 1+i0MaxLength)
                li = []
                if s[i0]=="0":
                    i1MaxLength = 1
                elif int(s[i0]) > 2:
                    i1MaxLength = 2
                else:
                    i1MaxLength = 3
                li.append(s[0:i0])
                if int(li[0]) > 255:
                    li.pop()
                    break
                for i1 in range(i0+1, min(n-1, i0+1+i1MaxLength)):
                    if s[i1]=="0":
                        i2MaxLength = 1
                    elif int(s[i1]) > 2:
                        i2MaxLength = 2
                    else:
                        i2MaxLength = 3
                    li.append(s[i0:i1])
                    if int(li[1]) > 255:
                        li.pop()
                        break
                    for i2 in range(i1+1, min(n, i1+1+i2MaxLength)):
                        li.append(s[i1:i2])
                        li.append(s[i2:])
                        if li[3]!="0" and s[i2]=="0": # 0이 아닌데 0으로 시작하면: .01 out
                            li.pop()
                            li.pop()
                            continue
                        if int(li[3]) > 255:
                            li.pop()
                            li.pop()
                            continue
                        if int(li[2]) > 255:
                            li.pop()
                            li.pop()
                            break
                        res.append(".".join(li))
                        li.pop()
                        li.pop()
                    li.pop()
                li.pop()
            return res
        else:
            return []