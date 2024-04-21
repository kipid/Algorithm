class Trie:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:
        cur=self.root
        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]
        cur['isWord']=word
        # print(f"insert :: {self.root = }")

    def remove(self, word: str) -> bool:
        cur=self.root
        stack = []
        for letter in word:
            if letter not in cur:
                return False
            stack.append((cur, letter))
            cur=cur[letter]
        res = 'isWord' in cur
        if res:
            del cur['isWord']
        while stack:
            if len(cur)==0:
                cur, letter = stack.pop()
                # print(f"len(cur)==0, {cur = }, {letter = }")
                del cur[letter]
            else:
                break
        # print(f"remove :: {self.root = }")
        return res

    def search(self, word: str) -> bool:
        cur=self.root
        for letter in word:
            if letter not in cur:
                return False
            cur=cur[letter]
        return 'isWord' in cur
        
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur=cur[letter]
        return True


# Your Trie object will be instantiated and called as such:
words = ["apple", "app", "ap", "aaaaa", "aaaa", "aaa", "aa", "a"]
obj = Trie()
for word in words:
    obj.insert(word)
# obj.remove("aaaaa")
# print(f"{obj.remove('apple') = }")
obj.remove("aaa")
obj.remove("aa")
obj.remove("a")
obj.remove("aaaaaa")
obj.remove("aaaaa")
obj.remove("aaaa")
