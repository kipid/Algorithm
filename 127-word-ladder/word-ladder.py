class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        ladderDict = defaultdict(list)
        for i in range(1, n + 1):
            ladderDict[beginWord[:i-1]+"*"+beginWord[i:]].append(beginWord)
        for word in wordList:
            for i in range(1, n + 1):
                ladderDict[word[:i-1]+"*"+word[i:]].append(word)
        # print(f"{ladderDict = }")
        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        while q:
            curr, count = q.popleft()
            if curr == endWord:
                return count
            for i in range(1, n + 1):
                for word in ladderDict[curr[:i-1]+"*"+curr[i:]]:
                    if word not in visited:
                        if word == endWord:
                            return count + 1
                        visited.add(word)
                        q.append((word, count + 1))
        return 0