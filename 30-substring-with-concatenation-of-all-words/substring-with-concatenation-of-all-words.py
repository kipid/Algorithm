class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0 or len(words[0]) == 0:
            return []
        
        dict_ = dict()
        for word in words:
            if word in dict_:
                dict_[word] += 1
            else:
                dict_[word] = 1
        wordsLength = len(words[0])
        fullWordsLength = wordsLength * len(words)
        maxIndex = len(s) - fullWordsLength
        res = set()
        for i in range(0, maxIndex+1):
            if i in res:
                continue
            dict_copy = dict()
            matched = True
            k = i
            for _ in range(len(words)):
                key1 = s[k:k+wordsLength]
                dict_copy[key1] = dict_copy.get(key1, 0) + 1
                if dict_copy[key1] > dict_.get(key1, 0):
                    matched = False
                    break
                k += wordsLength
            if matched:
                res.add(i)
                i1 = i + wordsLength
                while i1 <= maxIndex and s[i1-wordsLength:i1] == s[k:k+wordsLength]:
                    res.add(i1)
                    i1 += wordsLength
                    k += wordsLength
            dict_copy.clear()
        return list(res)
