class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur=self.root
        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]
        cur['isWord']=True
        # print(f"{self.root = }")

    def search(self, word: str) -> bool:
        cur, k = self.root, 0
        q = [(cur, k)]
        while q:
            cur, k = q.pop()
            if k == len(word):
                if 'isWord' in cur:
                    return cur['isWord']
                else:
                    continue
            letter = word[k]
            if letter in cur:
                q.append((cur[letter], k + 1))
            elif letter == ".":
                for key in cur.keys():
                    if len(key) == 1:
                        q.append((cur[key], k + 1))

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)