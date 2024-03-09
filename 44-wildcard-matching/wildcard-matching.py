class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIndex,pIndex,starIndex,m=0,0,-1,0
        while sIndex<len(s):
            if pIndex<len(p) and (s[sIndex]==p[pIndex] or p[pIndex]=='?'):
                pIndex+=1
                sIndex+=1
            elif pIndex<len(p) and p[pIndex]=='*':
                starIndex=pIndex
                m=sIndex
                pIndex+=1
            elif starIndex!=-1:
                pIndex=starIndex+1
                m+=1
                sIndex=m
            else:
                return False
        while pIndex<len(p) and p[pIndex]=='*':
            pIndex+=1
        return pIndex==len(p)
