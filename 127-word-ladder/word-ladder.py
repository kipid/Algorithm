class Ladder:
    def __init__(self, beginWord = "", count = 1, anotherLadder = None):
        if isinstance(anotherLadder, self.__class__):
            self.curr = anotherLadder.curr
            self.count = anotherLadder.count
        else:
            self.curr = beginWord
            self.count = count

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
        q = deque([Ladder(beginWord)])
        while q:
            ladder = q.popleft()
            if ladder.curr == endWord:
                return ladder.count
            for i in range(1, n + 1):
                for word in ladderDict[ladder.curr[:i-1]+"*"+ladder.curr[i:]]:
                    if word not in visited:
                        if word == endWord:
                            return ladder.count + 1
                        newLadder = Ladder(anotherLadder = ladder)
                        newLadder.curr = word
                        visited.add(word)
                        newLadder.count += 1
                        q.append(newLadder)
        return 0