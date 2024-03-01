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
        for key in dict_.keys():
            i = 0
            k = s.find(key, i)
            while k != -1 and k <= maxIndex:
                dict_copy = dict()
                # for key0,val0 in dict_.items():
                #     dict_copy[key0] = val0
                dict_copy[key] = 1
                i = k
                matched = True
                for _ in range(1, len(words)):
                    k += wordsLength
                    key1 = s[k:k+wordsLength]
                    dict_copy[key1] = dict_copy.get(key1, 0) + 1
                    if dict_copy[key1] > dict_.get(key1, 0):
                        matched = False
                        break
                if matched:
                    res.append(i)
                k = s.find(key, i+1)
        return res
