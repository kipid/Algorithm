class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length = -1
        res = []
        start, end, line = 0, 1, ""
        for i in range(len(words)):
            length += 1 + len(words[i])
            if length > maxWidth:
                length -= 1 + len(words[i])
                end = i - 1
                if end - start > 0:
                    additionalSpace = (maxWidth - length) // (end - start)
                    additionalSpaceUntil = (maxWidth - length) % (end - start)
                    for k in range(start, end+1):
                        if k - start < additionalSpaceUntil:
                            line += words[k] + " " + " " * additionalSpace + " "
                        else:
                            line += words[k] + " " + " " * additionalSpace
                    res.append(line.strip())
                else:
                    # print(f"{maxWidth - length = }")
                    line += words[start] + " " * (maxWidth - length)
                    res.append(line)
                start = i
                length = len(words[i])
                line = ""
        for k in range(start, len(words)):
            line += words[k] + " "
        res.append(line.strip() + " " * (maxWidth - length))
        return res
