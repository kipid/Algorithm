class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIndex,pIndex,starIndex,sMark=0,0,-1,0
        while sIndex<len(s):
            if pIndex<len(p) and (s[sIndex]==p[pIndex] or p[pIndex]=='?'):
                pIndex+=1
                sIndex+=1
            elif pIndex<len(p) and p[pIndex]=='*':
                starIndex=pIndex
                sMark=sIndex
                pIndex+=1
            elif starIndex!=-1:
                pIndex=starIndex+1
                sMark+=1
                sIndex=sMark
            else:
                return False
        while pIndex<len(p) and p[pIndex]=='*':
            pIndex+=1
        return pIndex==len(p)
