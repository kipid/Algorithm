class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_break = [False] * (len(s) + 1)
        can_break[0] = True
        for start in range(len(s) + 1):
            if not can_break[start]:
                continue
            for word in wordDict:
                if s.startswith(word, start):
                    can_break[start + len(word)] = True
        return can_break[len(s)]