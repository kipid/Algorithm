class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(curr: str, memo={}) -> bool:
            if curr in memo:
                return memo[curr]
            if not curr:
                return True
            
            for word in wordDict:
                if curr.startswith(word):
                    nxt = curr[len(word):]
                    if helper(nxt, memo):
                        memo[curr] = True
                        return True
            memo[curr] = False
            return False
        
        return helper(s)