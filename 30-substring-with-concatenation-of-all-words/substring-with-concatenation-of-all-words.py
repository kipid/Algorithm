class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dict_ = dict()
        for word in words:
            if word in dict_:
                dict_[word] += 1
            else:
                dict_[word] = 1
        wordsLength = len(words[0])
        fullWordsLength = wordsLength * len(words)
        maxIndex = len(s) - fullWordsLength
        res = []
        for i in range(0, maxIndex+1):
            key1 = s[i:i+wordsLength]
            dict_copy = dict()
            dict_copy[key1] = 1
            if dict_copy[key1] > dict_.get(key1, 0):
                matched = False
            else:
                matched = True
                k = i
                for _ in range(1, len(words)):
                    k += wordsLength
                    key1 = s[k:k+wordsLength]
                    dict_copy[key1] = dict_copy.get(key1, 0) + 1
                    if dict_copy[key1] > dict_.get(key1, 0):
                        matched = False
                        break
            if matched:
                res.append(i)
            dict_copy.clear()
        return res
